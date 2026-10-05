# Security policy

HireHub is an educational project. Do not use it with real personal information until it has received a security review.

## Reporting

Please do not publish credentials, personal documents or exploitable details in a public issue. Contact the repository maintainer privately if a private reporting channel is available.

## Deployment checklist

- Set a unique, strong `DJANGO_SECRET_KEY` through the hosting provider's environment settings.
- Set `DJANGO_DEBUG=False`.
- Set `DJANGO_ALLOWED_HOSTS` to the deployed hostnames only.
- Configure HTTPS and Django's production security settings.
- Review API permissions and protect personal/application data.
- Keep database backups private and uploaded media access-controlled.
