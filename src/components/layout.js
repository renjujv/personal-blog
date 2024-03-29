import * as React from "react"
import { Link } from "gatsby"

const Layout = ({ location, title, children }) => {
  const rootPath = `${__PATH_PREFIX__}/`
  const isRootPath = location.pathname === rootPath
  let header

  if (isRootPath) {
    header = (
      <h1 className="main-heading">
        <Link to="/">{title}</Link>
      </h1>
    )
  } else {
    header = (
      <Link className="header-link-home" to="/">
        {title}
      </Link>
    )
  }

  return (
    <div className="global-wrapper" data-is-root-path={isRootPath}>
      <header className="global-header">{header}</header>
      <main>{children}</main>
      <footer class='d-flex'>
        <div><hr/></div>
        <div class='d-flex f1'>
          <span class='f1'>©{new Date().getFullYear()}, Built with <a href="https://www.gatsbyjs.com">Gatsby</a></span>
          <Link class='f1 align-right' to="/rss.xml">RSS feed</Link>
        </div>
      </footer>
    </div>
  )
}

export default Layout
