
# Toasted Doom

~Run Doom on your toaster.~

This distilled/mutated edition of Doom is being shaped to help you run Doom on resource-constrained platforms, with an
emphasis on embedded environments.

The Doom 1 system requirements show 4 MB of RAM. Megabytes of RAM? What kind of toaster do you think I have?

I'm just starting out and learning about the Doom codebase, so things are being messed around with haphazardly.

Core goals include:

* Providing facilities to embed game data whenever possible
* Lower memory usage in favor of constant/static memory
* implementing configurable I/O abstract interfaces
  * Display
  * Input
  * Sound?
* Providing utilities to convert and downscale WADs