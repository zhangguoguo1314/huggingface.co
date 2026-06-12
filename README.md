---
title: 全自动签到助手
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
---

# 全自动助手

多网站多账号自动签到平台 — 一次配置，自动签到。

## 简介

全自动助手（Auto-Sign）是一个开源的自动签到平台。你可以：

- 在界面中添加要签到的网站和账号
- 设置定时任务（Cron 表达式）
- 系统到时间自动完成签到
- 签到结果记录在日志中，失败时可邮件/企业微信通知
- 可部署在电脑、服务器、甚至安卓手机上

---

## 技术栈

| 层级 | 技术 |
|------|------|
| **后端** | Python 3.11 + FastAPI + SQLAlchemy + APScheduler |
| **前端** | Vue 3 + TypeScript + Element Plus + Pinia + Vue Router + Vite |
| **数据库** | SQLite（单文件，无需单独部署） |
| **签到引擎** | 自定义 API 插件（urllib） |

---

## 功能特性

- 用户系统 — 注册、登录、JWT 认证
- 网站管理 — 添加/编辑/删除网站，支持多种网站类型
- 账号管理 — 添加账号、支持用户名密码/Token/Cookie
- 定时任务 — Cron 表达式调度，灵活设置签到时间
- 签到日志 — 查看每次签到结果，支持筛选和删除
- 邮件通知 — 签到失败自动发邮件提醒
- 企业微信机器人通知 — webhook 方式推送签到结果
- JSON 配置导入 — 从 AI 输出或他人模板直接粘贴导入
- 插件系统 — 支持自定义 Python 签到脚本

---

## API 接口

后端启动后，访问 `/docs` 查看完整的 Swagger API 文档。

主要接口：

| 路径 | 方法 | 说明 |
|------|------|------|
| `/api/auth/register` | POST | 用户注册 |
| `/api/auth/login` | POST | 用户登录（返回 JWT token） |
| `/api/sites` | GET/POST | 网站列表/添加网站 |
| `/api/sites/{id}/signin` | POST | 手动签到 |
| `/api/accounts` | GET/POST | 账号列表/添加账号 |
| `/api/tasks` | GET/POST | 任务列表/添加定时任务 |
| `/api/logs` | GET/DELETE | 签到日志/删除日志 |
| `/api/settings` | GET/PUT | 用户设置 |
| `/api/health` | GET | 健康检查 |

---

## 许可证

MIT License — 可自由使用、修改、分发。
