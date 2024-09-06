# Service Level Objectives (SLOs) for c397-team05-prod

This document defines the Service Level Objectives (SLOs) for the `c397-team05-prod` namespace. Each SLO includes a metric, a threshold, a target percentage, and an evaluation period.

## 1. HTTP Success Rate

- **Metric**: Percentage of successful HTTP requests.
- **Threshold**: 99.9% of HTTP requests should return a successful status code (2xx).
- **Target Percentage**: 99.9%
- **Evaluation Period**: Per month.

## 2. Page Load Time

- **Metric**: Percentage of page loads that complete within 0.5 seconds.
- **Threshold**: 95% of page loads should be completed within 0.5 seconds.
- **Target Percentage**: 95%
- **Evaluation Period**: Per week.

## 3. Uptime

- **Metric**: Percentage of uptime for the application in the `c397-team05-prod` namespace.
- **Threshold**: 99.95% uptime.
- **Target Percentage**: 99.95%
- **Evaluation Period**: Per month.

## 4. Latency

- **Metric**: Latency for critical API endpoints.
- **Threshold**: 95% of requests should have a latency of less than 200ms.
- **Target Percentage**: 95%
- **Evaluation Period**: Per month.

## 5. Database Availability

- **Metric**: Availability of the database service.
- **Threshold**: 99.95% availability.
- **Target Percentage**: 99.95%
- **Evaluation Period**: Per month.

## 6. CPU/Memory Utilization

- **Metric**: Percentage of time the CPU or Memory usage is below a defined threshold.
- **Threshold**: 95% of the time, CPU utilization should be below 80% and Memory usage below 75%.
- **Target Percentage**: 95%
- **Evaluation Period**: Per month.

## 7. Build Time

- **Metric**: Average build time for deployments.
- **Threshold**: 95% of builds should complete within 10 minutes.
- **Target Percentage**: 95%
- **Evaluation Period**: Per week.

## 8. Toil Reduction

- **Metric**: Percentage reduction in manual intervention for operational tasks.
- **Threshold**: Achieve a 20% reduction in manual toil.
- **Target Percentage**: 20%
- **Evaluation Period**: Per quarter.

## 9. Incident Resolution Time

- **Metric**: Median time to resolve critical incidents.
- **Threshold**: 95% of critical incidents should be resolved within 2 hours.
- **Target Percentage**: 95%
- **Evaluation Period**: Per month.

## 10. Percentage of Untested Code

- **Metric**: Percentage of code that has not been covered by automated tests.
- **Threshold**: Keep untested code below 10% of the codebase.
- **Target Percentage**: 90% of the codebase should be covered by tests.
- **Evaluation Period**: Per quarter.

### Conclusion

These SLOs are designed to ensure the reliability, performance, and user satisfaction of the services within the `c397-team05-prod` namespace. Regular monitoring and evaluation will help maintain and improve these metrics over time.
