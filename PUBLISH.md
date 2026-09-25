# 发布与同步流程

本文件记录 md3e-skill 仓库的 Git 推送、本地技能同步、发布包生成、GitHub Release 发布的完整流程。

> 工作区（源）：克隆到本地的仓库目录（下文用 `<repo>` 表示）
> 安装位置（目标）：`~/.codebuddy/skills/md3e`（Windows 为 `%USERPROFILE%\.codebuddy\skills\md3e`）
> 仓库地址：https://github.com/mfskys/md3e-skill
> 邮箱：使用 GitHub **noreply** 邮箱（在 GitHub → Settings → Emails 查看；避免 GH007）

以下示例中的 `D:\path\to\md3e` 仅为占位，请替换为你本机的实际克隆路径。

---

## 0. 前置检查

先确认 SKILL.md 的 metadata.version、变更记录和发布版本一致。2.0.0 的删除项属于破坏性变更。
在安装了 Python 与 PyYAML 的维护环境中运行仓库校验：

    python audit_run.py

普通源码修改不要求生成发布包；发布前生成 zip 后，按实际路径检查包内内容：

    python audit_run.py --archive ../dist/md3e.zip

日期和版本快照不随发布自动更新，只有核对来源后才修改其核对时间。

确认本地 Git 配置使用 noreply 邮箱（避免 GH007 邮箱隐私拦截）：

```powershell
cd D:\path\to\md3e
git config user.email "<your-id>+<your-login>@users.noreply.github.com"
git config user.name  "<your-github-login>"
```

---

## 1. 提交并推送代码到 GitHub

```powershell
cd D:\path\to\md3e
git add .
git commit -m "描述本次改动"
git push origin main
```

- 提交邮箱必须是 noreply 邮箱，否则 GitHub 会以 `GH007` 拒绝推送。
- 首次关联远程仓库时用 `git push -u origin main`，之后只需 `git push`。

---

## 2. 打 Tag 并推送（为 Release 准备）

```powershell
cd D:\path\to\md3e
git tag v2.0.0              # 当前版本示例；与 SKILL.md 的 metadata.version 保持一致
# 升级版本示例：
#   git tag v2.1.0          # 新功能
#   git tag v2.0.1          # 修 bug
git push origin v2.0.0
```

- Tag 是 Git 对某次 commit 的版本标记，Release 必须依赖一个 Tag。
- 推送 Tag 之后，Tag 出现在 GitHub，但还**不是** Release。

---

## 3. 生成发布包（md3e.zip）

发布包放在**仓库外**的目录（例如仓库同级的 `dist/`），避免污染仓库：

```powershell
$repo  = 'D:\path\to\md3e'
$dist  = Join-Path (Split-Path $repo -Parent) 'dist'
if (-not (Test-Path $dist)) { New-Item -ItemType Directory -Path $dist -Force }
Compress-Archive -Path (Join-Path $repo '*') -DestinationPath (Join-Path $dist 'md3e.zip') -Force
```

- 生成位置：`<repo的上级目录>\dist\md3e.zip`
- 用 `-Force` 覆盖旧包，每次发布前重新生成。
- 这个 zip 用于上传到 GitHub Release 的 "Attach binaries"，方便用户一键下载。
- **不要**把本机绝对路径、用户名等写进仓库内文档后再打包。

---

## 4. 创建 GitHub Release

1. 打开：https://github.com/mfskys/md3e-skill/releases/new
2. 填写：
   - **Choose a tag**：选刚推的 `v2.0.0`（或新版本号）
   - **Release title**：`MD3E Skill v2.0.0`
   - **Release description**：粘贴下方模板
   - **Attach binaries**：把上一步生成的 `md3e.zip` 拖进去
   - **Set as the latest**：勾上
3. 点 **Publish release**

### Release 描述模板

```markdown
Material Design 3 Expressive（MD3E）设计技能包

以设计意识、设计语言和设计判断为核心，适用于项目实际技术栈。

## 本次调整
- 强化设计哲学、价值观、原则、逻辑、策略与伦理
- 在合适位置复用 UI Kit；没有合适模式时根据规范与理念自主设计
- 按设计问题组织组件、样式、动效和 Token 参考资料
- Compose 包文档保留为按需读取的次要实现附录
- 移除主题生成器与四个 Kotlin 模板，使用项目已有主题设施
- 同步中英文说明与核心设计笔记

## 安装与升级
将 md3e/ 目录复制到 AI 助手支持的技能目录。
已有安装需按 CHANGELOG.md 清理旧生成器与模板；覆盖复制不会自动删除旧文件。
保留项目自定义内容后再清理，勿直接清空包含其他技能的父目录。

仓库: https://github.com/mfskys/md3e-skill
```

升级版本时改写 "新版本" 段落，列出本次新增/修复内容。

---

## 5. 同步到本地 CodeBuddy 技能目录

源码改动后，需要同步到本地安装位置才能生效：

```powershell
$src  = 'D:\path\to\md3e'
$dest = Join-Path $env:USERPROFILE '.codebuddy\skills\md3e'
New-Item -ItemType Directory -Path $dest -Force | Out-Null
Copy-Item -Path (Join-Path $src '*') -Destination $dest -Recurse -Force
```

- 安装位置：`%USERPROFILE%\.codebuddy\skills\md3e\`（用户级技能目录，对所有项目生效）
- 覆盖复制不会删除旧文件。升级时先核对 CHANGELOG.md 的移除清单，保留自定义内容，再清理安装目录中的对应旧文件。
- 同步后新开一个对话即可使用最新版本。

---

## 完整发布流程（一键顺序执行）

```powershell
$repo = 'D:\path\to\md3e'
cd $repo

# 1. 提交代码
git add .
git commit -m "release: v2.0.0"
git push origin main

# 2. 打 Tag
git tag v2.0.0
git push origin v2.0.0

# 3. 生成发布包
$dist = Join-Path (Split-Path $repo -Parent) 'dist'
if (-not (Test-Path $dist)) { New-Item -ItemType Directory -Path $dist -Force }
Compress-Archive -Path (Join-Path $repo '*') -DestinationPath (Join-Path $dist 'md3e.zip') -Force

# 4. 同步到本地技能目录
$dest = Join-Path $env:USERPROFILE '.codebuddy\skills\md3e'
New-Item -ItemType Directory -Path $dest -Force | Out-Null
Copy-Item -Path (Join-Path $repo '*') -Destination $dest -Recurse -Force

Write-Host "完成。接下来去 https://github.com/mfskys/md3e-skill/releases/new 创建 Release。"
```

---

## 版本号约定（SemVer）

- v2.0.0 → v2.1.0：新增功能（向下兼容）
- v2.0.0 → v2.0.1：修复问题（向下兼容）
- v2.0.0 → v3.0.0：破坏性改动（不向下兼容）
- 本次移除生成器与模板，准备版本为 2.0.0；源码更新不等同于已经发布 Release。

---

## 隐私注意

- 仓库内文档**不要**写入本机绝对路径、Windows 用户名、真实邮箱。
- Git 提交一律使用 GitHub noreply 邮箱。
- 发布 zip 前可快速自查：解压后搜索 `C:\Users`、本机盘符路径、真实姓名。
