from fastapi import FastAPI

app = FastAPI(
    title='FastAPI Heroku Template',
    description='HerokuでFastAPIによるWebAPIを作成するためのテンプレート',
    docs_url='/'
)


@app.get('/api')
def get_sample() -> str:
    return 'sample'


@app.post('/api/post')
def post_sample(sample: str):
    return sample
