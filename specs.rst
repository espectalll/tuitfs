--------------------
TuitFS Specification
--------------------

TuitFS relies on **documents**: static, unmutable strings, organized by tweets with hashtags,
replies and mentions which store the information and its metadata. Documents are declared with a
**header** tweet, which links to a **storage thread**. Each storage thread is composed of one or
more *storage tweets*, that contain the uploaded data. In order to do updates, a new storage thread
should be created (as a reply to the existing storage thread or as a completely new thread) with the
modified files reuploaded either entirely (for binary data) or as ``diff`` (for text files).

As a suggestion, a YAML file could be uploaded as ID 0 to indicate filenames and paths by ID.

Storage threads
~~~~~~~~~~~~~~~

::

	[@{username}] id:{integer};[data:{MIME};][base64,{Base64 string}][;eof[;id:...]];eot
	[@{username}] ~{split data, following the syntax on top}

An original storage thread, not being applied to an existing storage thread, is called a **storage
initialization thread**. Every storage thread being applied to an existing storage thread is a
**storage update thread**

In order to avoid polluting timelines, the uploader can mention themselves on any storage tweet,
which should hide the corresponding tweet on Twitter clients.

The ID of a file must be an integer. Negative, decimal or complex values are not allowed.

If data must be split between tweets, the oldest direct reply by the same user with ``~`` as its
first character will be picked up next. Tweets will then be concatenated "as is", without
breaklines. The last tweet found in a storage thread must contain an ``eot`` tag; otherwise, it is
considered as corrupted.

If no ``data`` tag is present, then ``text/plain`` is chosen as the default MIME type. Files on a
storage update thread with a previously existing ID of a ``text`` file and the ``text/x-diff`` type
are interpreted as text file patches and are applied over the currently existing data. Each text
file patch must indicate filename by ID. To upload patches as regular files, it is recommended to
use the ``text/x-patch`` content type in order to avoid problems.

Including data with a file is optional. Not including it, however, will have the same effect as if
the file didn't exist. This is useful for deleting files, as well as listing files that are yet to
be uploaded.

Text data must be encoded as UTF-8. Breaklines are forbidden on the tweets themselves.

Headers
~~~~~~~

In order to avoid polluting timelines, the uploader can mention themselves on any header tweet,
which should hide the corresponding tweet on Twitter clients.

Text can be added after the header is completed, with the only requirement of being separated
of the tweet URL or ID by a space character or a breakline. This can be used to describe a document
or an update, the latter being like Git commit messages.

::

	[@{username}] #tuitfs[-#new]:{tweet URL or ID}

Initialize a new document, and point out to the storage initialization thread.

::

	[@{username}] #tuitfs-#update:{tweet URL or ID}

Update an existing database with a new storage update thread.

File 0
~~~~~~

It is suggested to use the file with ID 0 on each storage initialization thread as a ``text/x-yaml`` containing
a set with entries corresponding to uploaded files, following this syntax:

::

	filenames:
		{file ID}: {[{path to}]filename}

A filename may have a maximum length of 255 bytes. A complete path may have any length. Any UTF-8
character is supported, albeit ``/`` can only be used to differentiate items in paths.

It is not mandatory to neither include this file, nor to indicate every file in the corresponding
document, neither to point only to existing files.

--------
Examples
--------

Here's the classic Hello World as a storage thread (of one tweet)

::

	id:1;base64,SGVsbG8gV29ybGQh;eot

If the storage tweet had the ID #123456789012345678, its header could look like:

::

	#tuitfs:https://twitter.com/myself/status/123456789012345678
	Trying out this hot new tech trend! Love it!

Or, if we just want to save the data without spreading the love to everyone:

::

	@myself #tuitfs-#new:123456789012345678

The same Hello World, but with an emoji and as a self-mention

::

	@myself id:1;base64,8J+RiyDwn4yNISDwn5i4;eot

Now we can reply to the original header with an update, if the new thread got ID 246913578024691356:

::

	@myself #tuitfs-#update:246913578024691356
	Now with some cute emojis! 😻

Hey! Not enough emojis! Let's fix this!

::

	@myself id:1;data:text/x-diff;base64,MWEyCj4g8J+SlfCfjonwn5GP8J+mivCfmYzwn46K8J+kmAo=;eof;

But wait! Aren't you fancy being an artist today...? Let's draw!
::

	@myself ~id:2;data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEASABIAAD//gATQ3JlYXRlZCB3aXRoIEdJTVD/2wBDAAoHBwgHBgoICAgLCgoLDhgQDg0NDh0VFhEYIx8lJCI

::

	@myself ~fIiEmKzcvJik0KSEiMEExNDk7Pj4+JS5ESUM8SDc9Pjv/2wBDAQoLCw4NDhwQEBw7KCIoOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Oz

...and so on, until the last tweet finally arrives:

::

	@myself ~NkmYzFAAAACMlMAmZZgACZG0OYAAHAmZmAaZmGyU04EgAeR;eof;eot

There you go! Let's publish the changes, then, by replying to the previous update:

::

	@myself #tuitfs-#update:493827156049382712
	More emojis! And a kitten! So 👌

Hmm, now that you think about it, you realize - this is a mess! How will people know what files are
they checking out? What if they open the cat drawing and can't figure out what it is because nobody
had conveniently labeled it? What a disaster!

We can now easily write a file 0:

::

	filenames:
		1: hello.txt
		2: cat.jpg

That should do it. Now it's just a storage thread and an update away!

::

	@myself ~id:0;data:text/x-yaml;base64,ZmlsZW5hbWVzOgoJMTogaGVsbG8udHh0CgkyOiBjYXQuanBnCg==;eot

As we're happy with the results, let's share it so everyone can enjoy!

::

	#tuitfs-#update:987654312098765424
	Cats are love! 😻 Cats are life! 😼

Great job there! Not only you got introduced to the magical world of TuitFS, you also have become a
world-famous artist! And all thanks to the power of Base64 strings splitted on tweets!1!

Anyway, you may also want to see live examples. Try out reading this very specs, you can find it as a
TuitFS document at https://rebrand.ly/tuitfs.
