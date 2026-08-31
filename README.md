# LLM Inference Course

一套面向推理系统初学者的 52 周实践课程。主线从 PyTorch 张量和 Transformer 前向开始，依次进入 Tiny-LLM、MLX/Metal、CUDA、Triton、Nano-vLLM 和 vLLM，最后完成一个可复现的推理实验项目。

## 学习目标

完成主线后，应当能够：

- 独立实现并验证一个小型 decoder-only Transformer；
- 解释 prefill、decode、KV cache、continuous batching、chunked prefill 和 paged KV；
- 为同一个算子建立 PyTorch oracle，并实现至少一个 Metal、CUDA 或 Triton 优化版本；
- 沿一条请求追踪 Nano-vLLM 和 vLLM 的调度、KV 管理与模型执行；
- 使用 TTFT、TPOT、吞吐、显存占用和尾延迟评价推理系统；
- 提交带环境记录、测试、原始结果和失败复盘的可复现实验。

## 硬件分工

| 环境 | 主要任务 | 不承担的任务 |
|---|---|---|
| M4 MacBook | PyTorch/MPS、MLX、Tiny-LLM、选择性 Metal kernel | CUDA、标准 Nano-vLLM/vLLM 性能结论 |
| CPU Linux | 单元测试、toy model、调度器模拟、API、load generator、代码阅读 | GPU kernel 性能结论 |
| NVIDIA Linux | CUDA、Triton、FlashAttention、Nano-vLLM、vLLM、真实性能实验 | 无 GPU 时不要用 CPU 结果代替 |

## 使用方式

1. 阅读 [ROADMAP.md](ROADMAP.md)，确认当前阶段和本周主题。
2. 从 `curriculum/` 中打开对应周文档。
3. 小型、一次性的练习放在 `labs/`。
4. 会跨多周演进的实现放在 `projects/`。
5. 所有性能结论使用 `benchmarks/` 中固定的 workload 和结果格式。
6. 每个阶段结束后在 `reports/` 完成阶段总结。

建议每周投入约 8 小时：2 小时阅读，4–5 小时编码，1–2 小时测试和 benchmark，剩余时间记录结论。课程按验收标准推进，不要求严格按日历赶进度。

## 仓库结构

```text
curriculum/   52 周课程和每周验收标准
labs/         可丢弃、可重做的小型练习
projects/     跨阶段持续演进的作品
benchmarks/   workload、结果 schema 和实验报告
tests/        跨项目测试规范
environments/ 各平台独立环境说明
upstreams/    外部仓库 URL、路径和 commit 记录
notes/        概念、论文和调试笔记
reports/      阶段总结
scripts/      环境与课程结构检查工具
artifacts/    模型、profile 等大文件；默认不提交
```

## 三条晋级规则

- 不能独立推导 tensor shape 时，不进入 kernel 优化。
- 没有正确性 oracle 和同步 benchmark 时，不声称性能提升。
- 画不出 scheduler、block table 和 KV page 生命周期时，不深入 vLLM 大仓库。

## 当前进度

- [ ] Phase 1：PyTorch 与 Transformer 基础（W01–W10）
- [ ] Phase 2：Tiny-LLM 与 serving 核心（W11–W28）
- [ ] Phase 3：工程与测量（W29–W32）
- [ ] Phase 4：CUDA（W33–W36）
- [ ] Phase 5：Triton（W37–W40）
- [ ] Phase 6：Nano-vLLM（W41–W44）
- [ ] Phase 7：vLLM（W45–W48）
- [ ] Phase 8：毕业项目（W49–W52）
