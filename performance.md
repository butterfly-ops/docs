# Performance

Butterfly is a high performance-first system. Butterfly framework and it's core features are built with Performance in mind.
You can check the following performance instructions:

## Opcache

As you may know, php is a scripting language which is processed and run by C code behind the scenes. When opcache is not enabled on your
web server, in each server request, your code is re-read and processed which is a massive operation if we get 100.000's of requests in seconds.

Enabling opcache on production cache's the opcode and re-use it from memory.

## Datalayer Caching

To be build a performant application, your queries should be optimized; but after optimizing your queries, next step should be
caching queries to reduce connection counts between web-application and database. You can check `Cache` section for more information.

## webp

`webp` is an image format developed by Google for web. `webp` format is not supported by all browser, but since it has a big improvement
on image file sizes, we highly recommend you to use it.

`Butterfly` supports webp natively, which means that, if you enable Webp Support for a specific `Image Config`, an image file ending with .`webp`
extension will be uploaded to same location with the original image.

You can follow next steps to enable webp in your application:

1. Upgrade your Butterfly setup to 1.5.170+

2. Enable Webp Support from /admin/cms_image_upload/list in `Admin Panel`

3. Run `bin/butterfly image:webp:generate` command to generate images for previously uploaded files.

4. Usage:

Frontend:

For frontend, we have to twig functions to call images: [`image`](https://thebutterfly.io/docs/#/frontend?id=image) and [`image_source`](https://thebutterfly.io/docs/#/frontend?id=image_source).

Webservices:

If you are using default ElasticSearch or Data Sources to get data, image fields automatically includes all sub-sizes as a key -> value array. You can retrieve
field ending with `_webp` to check whether webp version of the image exists or not.

If you are using Database, you need to be sure that, related image config has "Webp Support Enabled". You can also verify images by adding .webp at the end of the url.
After verification, you can basically add `.webp` at the end of current urls.

> [!WARNING]
> When you enable `Webp Support` for a previously used alias, images are not generated automatically.
> You need to run `bin/butterfly image:webp:generate` command to generate images.