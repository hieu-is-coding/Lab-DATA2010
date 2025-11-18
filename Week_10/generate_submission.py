"""
Automated script for the lab: generate synthetic feature CSVs, run analysis, and
save three required figures into `VinUni_Lecture/submission/`.

Produces:
 - submission/hist_surface_to_volume_mug.png
 - submission/heatmap_correlation.png
 - submission/ranking_top_features.png

Run from repo root:
    python VinUni_Lecture/generate_submission.py

"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

sns.set(style='whitegrid')

ROOT = Path('.')
OUT_DIR = ROOT / 'VinUni_Lecture' / 'submission'
FV_DIR = ROOT / 'feature_vectors'
OUT_DIR.mkdir(parents=True, exist_ok=True)
FV_DIR.mkdir(parents=True, exist_ok=True)

# --- Synthetic data generator (same defaults as handout) ---
def make_cat(cat, n=200):
    if cat == 'table':
        sa = np.random.normal(500, 80, n).clip(50, 2000)
        vol = np.random.normal(200, 40, n).clip(5, 1000)
    elif cat == 'mug':
        sa = np.random.normal(120, 30, n).clip(10, 800)
        vol = np.random.normal(45, 15, n).clip(1, 400)
    elif cat == 'lamp':
        sa = np.random.normal(180, 60, n).clip(10, 1200)
        vol = np.random.normal(60, 25, n).clip(1, 500)
    elif cat == 'club':
        sa = np.random.normal(90, 25, n).clip(10, 600)
        vol = np.random.normal(35, 12, n).clip(1, 300)
    else:  # dining
        sa = np.random.normal(300, 70, n).clip(20, 1500)
        vol = np.random.normal(120, 30, n).clip(1, 800)

    mean_curv = np.random.normal(25, 7, n).clip(0, 100) * (1 + (np.log1p(sa)/10 - 1))
    median_curv = mean_curv * (0.9 + 0.2*np.random.rand(n))
    silhouette_complexity = np.random.normal(10, 5, n).clip(0, 50)
    skeleton_complexity = np.random.normal(8, 4, n).clip(0, 50)
    aspect_ratio_y = np.random.normal(1.0 + (vol/500), 0.15, n).clip(0.2, 10)
    hollow_ratio = np.random.beta(2,5, n) * (1 + sa/2000)
    surface_to_volume_ratio = sa / (vol + 1e-6)

    df = pd.DataFrame({
        'mean_curvature': mean_curv,
        'median_curvature': median_curv,
        'surface_area': sa,
        'volume': vol,
        'silhouette_complexity': silhouette_complexity,
        'skeleton_complexity': skeleton_complexity,
        'aspect_ratio_y': aspect_ratio_y,
        'hollow_ratio': hollow_ratio,
        'surface_to_volume_ratio': surface_to_volume_ratio,
    })
    df['category'] = cat
    df['source_file'] = [f"{cat}_{i:04d}.obj" for i in range(len(df))]
    return df

# generate CSVs if folder empty
cats = ['club', 'dining', 'lamp', 'mug', 'table']
if not any(FV_DIR.glob('*_features.csv')):
    print('No feature CSVs found; generating synthetic data into', FV_DIR)
    np.random.seed(0)
    for c in cats:
        dfc = make_cat(c, n=200)
        dfc.to_csv(FV_DIR / f"{c}_features.csv", index=False)
else:
    print('Found existing CSVs in', FV_DIR)

# Load all CSVs
csvs = sorted(FV_DIR.glob('*_features.csv'))
dfs = []
for p in csvs:
    try:
        df = pd.read_csv(p)
        df['category'] = p.stem.split('_')[0]
        dfs.append(df)
    except Exception as e:
        print('Failed to read', p, e)

if not dfs:
    raise SystemExit('No data available after generation/reading.')

all_df = pd.concat(dfs, ignore_index=True, sort=False)
numeric_cols = all_df.select_dtypes(include=[np.number]).columns.tolist()

def find_column_like(df, keywords):
    """Return first column name containing all keywords (case-insensitive, underscores ignored)."""
    if df is None:
        return None
    cols = df.columns.tolist()
    keys = [k.lower().strip() for k in keywords]
    for c in cols:
        cl = c.lower().replace('_', ' ')
        if all(k in cl for k in keys):
            return c
    return None

# --- Figure 1: Histogram (surface-to-volume-like column for mugs) ---
hist_col = find_column_like(all_df, ['surface', 'volume']) or find_column_like(all_df, ['surface-to-volume'])
if hist_col is None:
    # fallback: pick a numeric column
    numeric_cols = all_df.select_dtypes(include=[np.number]).columns.tolist()
    if not numeric_cols:
        raise SystemExit('No numeric columns available to plot histogram.')
    hist_col = numeric_cols[0]
    print('Using fallback numeric column for histogram:', hist_col)
cat_name = 'mug'
vals = pd.to_numeric(all_df[all_df['category'] == cat_name][hist_col], errors='coerce').dropna()
plt.figure(figsize=(8,4))
sns.histplot(vals, bins=30, kde=True, color='tab:blue')
plt.title('Surface-to-Volume Ratio - mugs')
plt.xlabel(hist_col)
plt.ylabel('Count')
plt.grid(alpha=0.3)
fn1 = OUT_DIR / 'hist_surface_to_volume_mug.png'
plt.tight_layout()
plt.savefig(fn1, dpi=150)
plt.close()
print('Saved histogram to', fn1)

# --- Figure 2: Correlation heatmap (top numeric features) ---
numeric_cols = all_df.select_dtypes(include=[np.number]).columns.tolist()
cols_for_corr = [c for c in numeric_cols if c not in ['aesthetic_proxy']][:20]
corr = all_df[cols_for_corr].corr()
plt.figure(figsize=(10,8))
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, cmap='vlag', annot=True, fmt='.2f')
plt.title('Correlation heatmap')
fn2 = OUT_DIR / 'heatmap_correlation.png'
plt.tight_layout()
plt.savefig(fn2, dpi=150)
plt.close()
print('Saved heatmap to', fn2)

# --- Figure 3: Ranking chart (simple importance proxy using variance) ---
# Compute importance as variance across shapes (simple proxy for demonstration)
var = all_df[cols_for_corr].var().sort_values(ascending=False)
rank_df = pd.DataFrame({'feature': var.index, 'importance': var.values})
top_n = min(15, len(rank_df))
df_plot = rank_df.sort_values('importance', ascending=True).tail(top_n)
plt.figure(figsize=(8, max(4, 0.25*len(df_plot))))
plt.barh(df_plot['feature'], df_plot['importance'], color='tab:blue')
plt.xlabel('Variance (proxy importance)')
plt.title('Top features - horizontal ranking (variance proxy)')
fn3 = OUT_DIR / 'ranking_top_features.png'
plt.tight_layout()
plt.savefig(fn3, dpi=150)
plt.close()
print('Saved ranking chart to', fn3)

# Print short summary of generated outputs
print('\nSummary:')
print(' total samples:', len(all_df))
print(' numeric features:', len(numeric_cols))
print(' output images in', OUT_DIR)

# list saved files
for f in OUT_DIR.iterdir():
    print(' -', f.name)

print('\nDone.')
