import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="the_saga_stepfunction",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "the_saga_stepfunction"},
    packages=setuptools.find_packages(where="the_saga_stepfunction"),

    install_requires=[
        "aws-cdk.core==1.60.0",
        "aws-cdk.aws_apigateway==1.60.0",
        "aws-cdk.aws-lambda==1.60.0",
        "aws-cdk.aws-dynamodb==1.60.0",
        "aws-cdk.aws-stepfunctions==1.60.0",
        "aws-cdk.aws-stepfunctions-tasks==1.60.0",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
