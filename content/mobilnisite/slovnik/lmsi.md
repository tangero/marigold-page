---
slug: "lmsi"
url: "/mobilnisite/slovnik/lmsi/"
type: "slovnik"
title: "LMSI – Local Mobile Station Identity"
date: 2025-01-01
abbr: "LMSI"
fullName: "Local Mobile Station Identity"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lmsi/"
summary: "Dočasný identifikátor přidělený mobilní stanici (UE) návštěvnickým registrem polohy (VLR) pro místní správu v rámci jeho servisní oblasti. Používá se k jednoznačné adresaci účastníka pro signalizaci a"
---

LMSI je dočasný identifikátor přidělený návštěvnickým registrem polohy (VLR), který jednoznačně adresuje mobilní stanici v rámci její místní servisní oblasti pro signalizaci, čímž zvyšuje bezpečnost snížením přenosu trvalého IMSI po rozhraní vzduch.

## Popis

Local Mobile Station Identity (LMSI) je dočasný identifikátor přidělený sítí, používaný v jádrových sítích GSM a UMTS pro přepojování okruhů. Jedná se o 4oktetové (32bitové) číslo přidělené návštěvnickým registrem polohy (VLR) při registraci mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) v jeho servisní oblasti, typicky během procedur aktualizace polohy. LMSI je uloženo jak ve VLR, tak v domovském registru polohy ([HLR](/mobilnisite/slovnik/hlr/)) jako součást profilu účastníka. Jeho primární architektonická role je poskytnout kratší, lokálně významný ukazatel pro MS, což umožňuje VLR efektivně spravovat a odkazovat se na účastníka bez opakovaného používání International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)). LMSI se používá interně v síti pro operace indexování a vyhledávání v databázích, zejména když VLR potřebuje načíst data účastníka z HLR nebo během předávání mezi VLR. Nepoužívá se přes rozhraní vzduch; pro zabezpečení tohoto rozhraní se místo toho používá Temporary Mobile Subscriber Identity (TMSI). Přítomnost LMSI optimalizuje signalizaci tím, že umožňuje rychlejší vyhledávání v databázích a snižuje režii zpracování spojenou s delšími trvalými identifikátory. Je klíčovou součástí oddělení identity účastníka od dočasných identifikátorů na rádiové úrovni, což přispívá k celkové bezpečnosti a škálovatelnosti mobilních sítí 2G a 3G.

## K čemu slouží

LMSI bylo zavedeno, aby řešilo neefektivitu a bezpečnostní obavy spojené s používáním trvalého [IMSI](/mobilnisite/slovnik/imsi/) pro časté síťové operace. V raných mobilních sítích neustálý přenos nebo zpracování dlouhého IMSI pro identifikaci účastníka během aktualizací polohy, navazování hovorů a dotazů do databází vytvářelo významnou signalizační režii a zvyšovalo zranitelnost vůči sledování a odposlechu. LMSI to řeší tím, že poskytuje lokální, dočasný identifikátor, který má význam pouze v rámci administrativní domény konkrétního VLR. To umožňuje síti provádět interní správu a signalizaci pomocí stručného identifikátoru, čímž se snižuje doba vyhledávání v databázích a minimalizuje se vystavení trvalého IMSI. Historicky byla součástí vrstvené strategie správy identit, která zahrnovala TMSI pro ochranu rádiového rozhraní a LMSI pro efektivitu jádrové sítě. Řešila omezení dřívějších přístupů, kterým chyběly takové podrobné dočasné identifikátory, a umožnila škálovatelnější a bezpečnější správu účastníků s exponenciálním růstem jejich počtu v sítích.

## Klíčové vlastnosti

- Dočasný 32bitový identifikátor přidělený VLR
- Používá se výhradně v jádrové síti pro přepojování okruhů (ne přes rozhraní vzduch)
- Uložen v záznamech účastníka jak ve VLR, tak v HLR
- Umožňuje efektivní indexování databází a načítání dat účastníka
- Snižuje signalizační režii tím, že se vyhýbá častému používání IMSI
- Zvyšuje bezpečnost minimalizací vystavení trvalého identifikátoru v jádrové signalizaci

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [LMSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/lmsi/)
