### Simple Chain

```txt
     +-------------+       
     | PromptInput |       
     +-------------+       
            *              
            *              
            *              
    +----------------+     
    | PromptTemplate |     
    +----------------+     
            *              
            *              
            *              
      +----------+         
      | ChatGroq |         
      +----------+         
            *              
            *              
            *              
   +-----------------+     
   | StrOutputParser |     
   +-----------------+     
            *              
            *              
            *              
+-----------------------+  
| StrOutputParserOutput |  
+-----------------------+
```

### Sequential Chain
```
     +-------------+       
     | PromptInput |       
     +-------------+       
            *              
            *              
            *              
    +----------------+     
    | PromptTemplate |     
    +----------------+     
            *              
            *              
            *              
      +----------+         
      | ChatGroq |         
      +----------+         
            *              
            *              
            *              
   +-----------------+     
   | StrOutputParser |     
   +-----------------+     
            *              
            *              
            *              
+-----------------------+  
| StrOutputParserOutput |  
+-----------------------+  
            *              
            *              
            *              
    +----------------+     
    | PromptTemplate |     
    +----------------+     
            *              
            *              
            *              
      +----------+         
      | ChatGroq |         
      +----------+         
            *              
            *              
            *              
   +-----------------+     
   | StrOutputParser |     
   +-----------------+     
            *              
            *              
            *              
+-----------------------+  
| StrOutputParserOutput |  
+-----------------------+  
```



### Parallel Chain

```mermaid
graph TD
    A[ Topic] --> B(Prompt 1)
    A --> C(Prompt 2)
    B --> |Model 1| D(Notes)
    C --> |Model 2| E(Quiz)
    D --> |Prompt 3| G(Model)
    E --> G(Model)
    G --> H(Output)
```

*prompt 3 we can joint any chain



```ascii
           +--------------------------+            
           | Parallel<note,quiz>Input |            
           +--------------------------+            
                ***             ***                
              **                   **              
            **                       **            
+----------------+              +----------------+ 
| PromptTemplate |              | PromptTemplate | 
+----------------+              +----------------+ 
          *                             *          
          *                             *          
          *                             *          
    +----------+                  +----------+     
    | ChatGroq |                  | ChatGroq |     
    +----------+                  +----------+     
          *                             *          
          *                             *          
          *                             *          
+-----------------+            +-----------------+ 
| StrOutputParser |            | StrOutputParser | 
+-----------------+            +-----------------+ 
                ***             ***                
                   **         **                   
                     **     **                     
          +---------------------------+            
          | Parallel<note,quiz>Output |            
          +---------------------------+            
                         *                         
                         *                         
                         *                         
                +----------------+                 
                | PromptTemplate |                 
                +----------------+                 
                         *                         
                         *                         
                         *                         
                   +----------+                    
                   | ChatGroq |                    
                   +----------+                    
                         *                         
                         *                         
                         *                         
                +-----------------+                
                | StrOutputParser |                
                +-----------------+                
                         *                         
                         *                         
                         *                         
            +-----------------------+              
            | StrOutputParserOutput |              
            +-----------------------+         
```

### Conditional Chain

```mermaid
graph TD
    A[Feedback] --> |Positive / Negative| B(Analyze)
    B --> C(Positive)
    B --> D(Negative)
    C --> Feedback_Thank_You
    D --> Email_Sorry_for_Reason
```

```ascii
[Input Text] 
      │
      ▼
┌──────────────┐
│  Classifier  │ Parses text into a Pydantic object (Positive/Negative)
└──────┬───────┘
       │ Passes Pydantic object
       ▼
┌──────────────┐
│RunnableBranch│ Evaluates conditions sequentially
└──────┬───────┘
       ├─► If "Positive" ──► [Positive Prompt] ──► [Model] ──► [Output]
       ├─► If "Negative" ──► [Negative Prompt] ──► [Model] ──► [Output]
       └─► Otherwise     ──► [Fallback Lambda] ──► [Output]
```