# Django Playground

- Djangoのアプリケーションに関する実験場

## コマンド類

### コードフォーマット

```bash
tox -e format
```

### テスト

```bash
tox run-parallel --skip-env format
```

### 全部やる

```bash
tox
```

## 実験の成果（順不同）

- `Choices` クラスの調査
- toxの調査
- プロパティベーステストライブラリ`Hypothesis`の導入
- Modelのバリデーションについて
