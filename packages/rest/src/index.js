const Koa = require('koa')
const Router = require('koa-router')
const bodyParser = require('koa-bodyparser')

const app = new Koa()
const router = new Router()

const user = {
  accountId: 'e8a2e924-b52e-44ee-b5b5-06bf48feb80c',
  name: 'Adam',
  org: 'Bulb',
  pod: 'Platform',
}

app.use(bodyParser())

router.get('/accounts', (ctx) => {
  ctx.status = 200
  ctx.body = JSON.stringify(user)
})

router.post('/accounts', (ctx) => {
  ctx.status = 200
  ctx.body = {
    accountId: 'a0a0a000-a00a-00aa-a0a0-00aa00aaa00a',
    ...ctx.request.body,
  }
})

app.use(router.routes()).listen(3000)
