## Week 13 — GPU Computing for Data Science

Focus: move simple tensor workloads to the GPU and measure speed differences with PyTorch.

### Tasks (complete in `submission_template/Week13_Tasks.ipynb`)
- Detect whether CUDA is available and report device information.
- Benchmark a matrix multiplication on CPU vs GPU (if available) and compare timings.
- Train a tiny logistic-regression classifier on synthetic data using the GPU when present, and report timing + loss.

### Submission
- Submit only the completed `Week13_Tasks.ipynb`.
- Keep code runnable on CPU-only machines; guard GPU-specific code with availability checks.
