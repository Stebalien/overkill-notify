from setuptools import setup, find_packages
setup(
    name = "overkill-extra-notify",
    version = "0.1",
    install_requires=["overkill", "notify2"],
    packages = find_packages(),
    namespace_packages = ["overkill", "overkill.extra"],
    author = "Steven Allen",
    author_email = "steven@stebalien.com",
    description = "Notification helper for overkill.",
    license = "GPL3",
    url = "http://stebalien.com"
)
