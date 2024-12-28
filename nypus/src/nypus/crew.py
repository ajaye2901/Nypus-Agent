from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Nypus():
	"""Nypus crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def trend_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['trend_researcher'],
			verbose=True
		)

	@agent
	def blogger(self) -> Agent:
		return Agent(
			config=self.agents_config['blogger'],
			verbose=True
		)
	
	@agent
	def seo_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['seo_writer'],
			verbose=True
		)
	
	@agent
	def commercial_script_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['commercial_script_writer'],
			verbose=True
		)

	@agent
	def hashtag_specialist(self) -> Agent:
		return Agent(
			config=self.agents_config['hashtag_specialist'],
			verbose=True
		)
	
	@agent
	def ecommerce_product_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['ecommerce_product_writer'],
			verbose=True
		)
	
	@agent
	def short_form_scriptwriter(self) -> Agent:
		return Agent(
			config=self.agents_config['short_form_scriptwriter'],
			verbose=True
		)
	
	@agent
	def keyword_blog_topic_creator(self) -> Agent:
		return Agent(
			config=self.agents_config['keyword_blog_topic_creator'],
			verbose=True
		)
	
	@agent
	def video_ad_idea_creator(self) -> Agent:
		return Agent(
			config=self.agents_config['video_ad_idea_creator'],
			verbose=True
		)
	
	@agent
	def press_release_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['press_release_writer'],
			verbose=True
		)
	
	@agent
	def seo_auditor(self) -> Agent:
		return Agent(
			config=self.agents_config['seo_auditor'],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def blog_task(self) -> Task:
		return Task(
			config=self.tasks_config['blog_task'],
			output_file='blog.md'
		)
	
	@task
	def seo_article_task(self) -> Task:
		return Task(
			config=self.tasks_config['seo_article_task'],
			output_file='article.md'
		)
	
	@task
	def commercial_script_task(self) -> Task:
		return Task(
			config=self.tasks_config['commercial_script_task'],
			output_file='spot_script.md'
		)

	@task
	def hashtag_suggestion_task(self) -> Task:
		return Task(
			config=self.tasks_config['hashtag_suggestion_task'],
			output_file='hashtags.md'
		)
	
	@task
	def product_description_task(self) -> Task:
		return Task(
			config=self.tasks_config['product_description_task'],
			output_file='prod_desc.md'
		)
	
	@task
	def short_form_script_task(self) -> Task:
		return Task(
			config=self.tasks_config['short_form_script_task'],
			output_file='vdo_scripts.md'
		)
	
	@task
	def keyword_blog_topic_task(self) -> Task:
		return Task(
			config=self.tasks_config['keyword_blog_topic_task'],
			output_file='keyword-blog-topic.md'
		)
	
	@task
	def video_ad_idea_task(self) -> Task:
		return Task(
			config=self.tasks_config['video_ad_idea_task'],
			output_file='vdo_ad_idea.md'
		)
	
	@task
	def press_release_task(self) -> Task:
		return Task(
			config=self.tasks_config['press_release_task'],
			output_file='press_release.md'
		)
	
	@task
	def seo_audit_task(self) -> Task:
		return Task(
			config=self.tasks_config['seo_audit_task'],
			output_file='seo_audit.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Nypus crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
