const Koa = require('koa')
const Router = require('koa-router')

const app = new Koa()
const router = new Router()

const routes = router.get('/', (ctx, next) => {
  ctx.body = JSON.stringify({
    message: 'Hello world',
  })
})

app.use(router.routes()).listen(3000)
