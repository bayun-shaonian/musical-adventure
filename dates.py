from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import pandas as pd
import os
from tempfile import NamedTemporaryFile
import matplotlib.pyplot as plt
app = FastAPI()

@app.post("/analyze/salary_by_district")
async def analyze_salary_by_district(file: UploadFile = File(...)):
    df = pd.read_csv('某招聘网站数据.csv')

    stats_df = df.groupby("district")["salary"].agg(
        平均值="mean",
        最小值="min",
        最大值="max"
    ).reset_index()


    with NamedTemporaryFile(suffix=".xlsx", delete=False) as temp_file:
        stats_df.to_excel(temp_file.name, index=False)
        temp_file_path = temp_file.name

    return FileResponse(
        path=temp_file_path,
        filename="地区薪资统计.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

@app.post("/analyze/company_count_chart")
async def company_count_chart(file: UploadFile = File(...)):
    df = pd.read_csv('某招聘网站数据.csv')
    company_count = df.groupby('district')['companyId'].nunique().reset_index()
    # 绘制柱状图
    plt.figure(figsize=(10, 6))
    plt.bar(company_count['district'], company_count['companyId'])
    plt.xlabel('地区')
    plt.ylabel('公司数量')
    plt.title('各地区公司数量分布')
    plt.xticks(rotation=45)
    # 保存图片
    img_path = "地区公司数量柱状图.png"
    plt.savefig(img_path, bbox_inches='tight')
    plt.close()
    # 返回图片
    return FileResponse(img_path, filename="地区公司数量柱状图.png")
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=9000)

