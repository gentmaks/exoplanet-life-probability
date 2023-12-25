This project is centered around acquiring proficiency in handling extensive datasets,
utilizing the Planets API provided by API-Ninjas. Our primary objective is to delve into
the intricacies of big data and develop skills in comparing and visualizing diverse
planetary attributes. By gathering data on different planets, we aim to construct graphs
that offer a clear and insightful representation of the information. The core focus is on
building an algorithm capable of comparing these planetary attributes against
user-defined limit margins. This algorithm, designed to determine the most probable
planet for life, assigns scores within specific ranges based on user-set criteria,
facilitating a more intuitive understanding. Through this process, we not only explore the
challenges of dealing with substantial datasets but also gain hands-on experience in
creating impactful visualizations. Moreover, the project serves as a practical application,
offering a unique opportunity to assess the habitability potential of various planets
beyond Earth by incorporating user-defined constraints into the analysis.

Various programming principles were used in order to achieve the success of this
project. Modularity and Object Oriented Programming were big parts of this project and
the blueprint of our code. Breaking our code down into functions that we could reuse
throughout our code and the utilization of classes (parent and child) and inheritance
allowed us to use different methods at different places without sacrificing time and
readability. Another important aspect of the project was importing different libraries into
our code in order to eliminate the need to write code from scratch. The libraries used in
our project were TKInter to help us construct basic graphical user interfaces and the
requests module to let us send HTTP requests and get responses from API calls.
Another library used was matplotlib which was crucial in graphing the results of the
planet attributes we got from the API calls. In order to run the code you need to be
subscribed to the Planets API.

The data we were working with on this project was data provided by the Planets API for
API-Ninjas. Passing queries into the call function gave us the opportunity to filter data
based on our needs. Because the data provided were attributes of planets then we can
safely assume that there is some sort of astrophysical law relation between these
attributes, for example as the mass of the host star of planets got bigger the
temperature of these stars got bigger also subsequently resulting in a higher planet
temperature if their period was low enough (meaning their distance from their
respective sun was low, resulting in them being closer to the sun).
