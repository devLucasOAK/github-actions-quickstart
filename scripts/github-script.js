module.exports = async ({ github, context, core }) => {
  const repos = await github.rest.repos.listForUser({
    username: context.repo.owner,
  });

  // filter only full_name
  const reposName = repos.data.map((repo) => repo.full_name);

  // set output
  core.exportVariable("REPOS", reposName);
};
