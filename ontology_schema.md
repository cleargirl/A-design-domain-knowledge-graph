Domain Knowledge Graph Ontology Specification
This repository adopts a lightweight engineering design ontology tailored for conceptual design knowledge extraction from patent abstracts.
1.1 Entity Type
The domain knowledge graph (dKG) consists of four primary entity types:
(1) DesignSubject
Definition:The unique product concept or system described in a patent abstract.
Role in the graph:Acts as the head entity and semantic anchor of each star-shaped subgraph.
Examples:“modular sewage treatment device”, “marine wastewater purification system”.
(2) Feature
Definition:Physical components, structural modules, or functional characteristics contained in the DesignSubject.
Examples:filtration membrane, heat exchanger, aeration module.
(3) TargetObject
Definition:External materials, media, or substances that the DesignSubject acts upon.
Examples:sewage, microplastics, heavy metal ions.
(4) Method
Definition:Working principles, technologies, or processes on which the DesignSubject is based.
Examples:biological degradation, membrane separation, photocatalytic oxidation.
1.2 Relation Types
The ontology defines three directed relation types:Relation	Domain → Range	Semantic Meaning
contain	DesignSubject → Feature	The DesignSubject includes or is composed of the Feature
act_on	DesignSubject → TargetObject	The DesignSubject acts upon or treats the TargetObject
based_on	DesignSubject → Method	The DesignSubject operates based on a specific Method
Each relation is explicitly modeled as a labeled edge in the knowledge graph.
1.3 Graph Structure
The initial graph is composed of star-shaped subgraphs, each centered on one DesignSubject.
Subgraphs extracted from different patents are later merged through entity fusion based on semantic similarity.
The final dKG is a multi-relational, heterogeneous graph suitable for relational graph attention networks (rGAT).
