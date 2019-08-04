import React from 'react'
import { gql } from 'apollo-boost'
import { Query } from 'react-apollo'
import './Accounts.css'

const GET_ACCOUNTS = gql`
  {
    account {
      name
      pod
    }
  }
`

export const Accounts = () => {
  return (
    <section>
      <h2>Accounts</h2>

      <Query query={GET_ACCOUNTS}>
        {({ loading, error, data }) => {
          if (loading) return <span>Loading…</span>
          if (error) return <span>There was an error</span>
          if (data && data.account)
            return (
              <section>
                <span className="block">
                  <strong>{data.account.name}</strong>
                </span>
                <span>{data.account.pod}</span>
              </section>
            )
        }}
      </Query>
    </section>
  )
}
