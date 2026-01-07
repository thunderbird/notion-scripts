The tests were last taken care of in 82dc73a8fd5bdae77294b75d1d4770fdfb10b328.
They were barely made to work just after 0fecd8b41acf150a78351c8dcb4df777770be24e

At the 82dc73a8, you can trigger them with `rye run test`. At the latest commit,
you can trigger them using `uv run task test`

As the code gets more complex it is more pressing to keep them running, so far
it has been neglected since this was more of a side project.

A number of features have been added since 82dc73a8, it would be useful to go
through the commit log and test each change.
