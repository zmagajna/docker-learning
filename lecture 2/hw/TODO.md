# TODO

1.) Create application(docker) with python code where at the beginning of execution the program takes all environment variable
and writes it to the DB in table call `envs`(columns `id`, `type`, `value`) `type` can is `DB`, `APP`

2.) From environment variable you set up the number on which our application will start counting(`os.getenv` returns the value in `string`!). Every number divided by 3 should be should be multiply by 1000 and every number divided by 5 should should return 0. When number is greater or equal 30 the counter number should start couting back from 0.

3.) Upper logic should also be saved to the DB in the table `numbers`.
