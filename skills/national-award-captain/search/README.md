# search — 文献检索入口（找相关论文）

按目的路由：
1. **模型/方法相关文献**（为模型选型找依据）：
   - OpenAlex（`https://api.openalex.org/works?search=<关键词>&per-page=5`，免费无 key）
   - CrossRef（`https://api.crossref.org/works?query=<关键词>&rows=5`）
   - arXiv（`https://export.arxiv.org/api/query?search_query=all:<关键词>&max_results=5`）
   - 也可复用 `<mmd>` 的 paper_search 子技能（OpenAlex，含摘要重建）。
2. **获奖/真题参考**（本地，零网络）：读 `<mmd>/references/Outstanding Thesis/{CUMCM, 2017MCM ICM}/`。
3. **期刊引用**：`nature-academic-search`（PubMed/CrossRef/arXiv + 引文核验）→ `nature-citation`（匹配 Nature/CNS 系列）。

## 产出格式
- 国赛论文：GB/T 7714（如 `[1] 张三, 李四. 题名[J]. 期刊, 2023, 45(2): 1-10.`；≥10 条）。
- 美赛论文：APA/Nature 风格（DOI 优先）。
- 每条附：作者/题名/来源/年份/DOI（如可得），写入正文参考文献节。

## 降级
- 无网络/接口失败 → 只用本地优秀论文库 + `<mm>/competitions/<comp>/phrase_bank.md` 兜底，并在 decision_log 记录。
- 严格要求：检索结果只作参考，不得整段照搬；引用必须真实（宁可少引不可编造 DOI）。