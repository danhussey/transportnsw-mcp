docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate \
    -i /local/tripplanner_swag_20231016_1.yaml  \
    -l python \
    -o /local/out/python