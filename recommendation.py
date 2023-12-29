from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_movie_recommendations(input_movie_name):
    # Load pretrained GPT-2 model and tokenizer
    model_name = "gpt2"  # You can experiment with other GPT-2 variants if needed
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Generate recommendations using the language model
    input_ids = tokenizer.encode(f"Based on the movie '{input_movie_name}', I recommend the following movies:", return_tensors="pt")
    output = model.generate(input_ids, max_length=100, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)

    # Decode and print the generated recommendations
    recommendations = tokenizer.decode(output[0], skip_special_tokens=True).strip()
    if recommendations:
        st.write("**Recommendations:**", recommendations)
    else:
        st.write("**Recommendations:** N/A")
