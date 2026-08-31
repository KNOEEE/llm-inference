# Scheduler Simulator

使用 CPU 和 scripted model 测试请求状态、token budget、continuous batching、chunked prefill、block allocation、page reuse 和 preemption。

核心价值是确定性：给定请求序列和 page pool，测试应能精确断言每一步 waiting/running 队列与 block table。

