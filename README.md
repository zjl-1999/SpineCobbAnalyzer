# SpineCobbAnalyzer

基于 Python + Tkinter 的脊柱 Cobb 角分析桌面软件。导入脊柱图像后，可进行 Cobb 角测量、侧向力（lateral force）与楔形截骨（wedge osteotomy）工况分析、边界条件与应力录入、矫正率计算，并生成帕累托前沿（Pareto Front）分析与 Word 报告；另带可选的 AI 辅助功能。

A Python/Tkinter desktop tool for spinal Cobb angle analysis. It imports spinal images, measures the Cobb angle, analyzes lateral-force and wedge-osteotomy cases, records boundary conditions and stress, computes correction rate, produces Pareto-front analysis, and exports Word reports. Optional AI assistance is available.

## 功能 / Features

- 脊柱图像导入与 Cobb 角测量
- 侧向力（lateral force）工况分析
- 楔形截骨（wedge osteotomy）工况分析
- 帕累托前沿（Pareto Front）分析
- 报告导出（Word / 图表）
- 可选 AI 辅助（Gemini / SiliconFlow / Claude / OpenAI）

## 环境要求 / Requirements

- Python 3.10 或 3.11（建议，部分依赖对最新版适配有限）
- 依赖见 `requirements.txt`

## 快速开始 / Quick Start

```bash
pip install -r requirements.txt
python Spine_COBB_Analyzer.py
```

国内下载依赖较慢时可使用清华镜像：

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

更详细的安装与排错说明见 `Installation and Usage.txt`。

## 数据 / Data

`data/` 目录包含示例数据（图像、Excel 表格与帕累托前沿数据表），用于演示各分析工况。

## 可选 AI 配置 / Optional AI

AI 功能完全可选，不配置也可使用全部分析功能。如需启用，请复制 `.env.example` 为 `.env` 并填入对应服务的 API Key。`.env` 已被 `.gitignore` 忽略，不会被提交。

## 安全说明 / Security Note

源码中的 `INVITE_SECRET`、`LICENSE_SECRET`、`ADMIN_REG_TOKEN`、`APP_SECRET_SALT` 已替换为 `CHANGE_ME_*` 占位符。重新分发或打包前，请改成你自己的随机值。注册邀请码机制默认开启（`INVITE_REQUIRED = True`）；如需允许任何人直接注册，可将其改为 `False`。

## 许可证 / License

[MIT](LICENSE)
