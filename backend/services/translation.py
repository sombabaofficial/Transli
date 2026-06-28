from typing import Optional
from services.translation_gemini import translate_gemini, summarize_gemini

async def translate_text(text: str, source_lang: str, target_lang: str, provider: str = "gemini", context: Optional[str] = None, glossary: Optional[str] = None) -> str:
    """Dispatcher for Translation providers."""
    print(f"[DEBUG TRANSLATION DISPATCHER] Dispatching translation to provider: {provider}")
    if provider == "nllb":
        from services.translation_nllb import translate_nllb
        try:
            return await translate_nllb(text, source_lang, target_lang, glossary=glossary)
        except ValueError as e:
            if str(e).startswith("NLLB_FALLBACK"):
                print(f"[TRANSLATION] NLLB fallback to Gemini: {e}")
                return await translate_gemini(text, source_lang, target_lang, context, glossary)
            raise
    else:
        return await translate_gemini(text, source_lang, target_lang, context, glossary)

async def summarize_text(text: str, provider: str = "gemini") -> str:
    """Dispatcher for Session Summarizer"""
    if provider == "nllb":
        print("[WARNING] NLLB cannot summarize. Falling back to Gemini.")
        return await summarize_gemini(text)
    else:
        return await summarize_gemini(text)
