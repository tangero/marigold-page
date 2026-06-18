---
slug: "lau"
url: "/mobilnisite/slovnik/lau/"
type: "slovnik"
title: "LAU – Location Area Update"
date: 2025-01-01
abbr: "LAU"
fullName: "Location Area Update"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lau/"
summary: "Procedura prováděná mobilním zařízením za účelem informování sítě o své aktuální polohové oblasti (LA), která umožňuje efektivní vyvolávání a správu mobility. Je spuštěna, když se zařízení přesune do"
---

LAU je procedura, při které mobilní zařízení informuje síť o své aktuální polohové oblasti (Location Area), aby bylo možné efektivní vyvolávání (paging) a správu mobility; je spuštěna při přesunu do nové oblasti nebo periodicky.

## Popis

Procedura aktualizace polohové oblasti (Location Area Update – LAU) je základním procesem správy mobility v GSM, UMTS a LTE (ačkoli v LTE byla nahrazena aktualizací sledované oblasti – Tracking Area Update). Polohová oblast ([LA](/mobilnisite/slovnik/la/)) je skupina buněk definovaná v rámci sítě. Jádrová síť, konkrétně návštěvnický lokální registr ([VLR](/mobilnisite/slovnik/vlr/)) a ústředna mobilní sítě ([MSC](/mobilnisite/slovnik/msc/)), sleduje LA uživatelského zařízení (UE), aby věděla, kde je má vyvolat pro transakce iniciované sítí. LAU je iniciována uživatelským zařízením, když zjistí (z vysílaných systémových informací), že vstoupilo do buňky patřící do nové LA.

Procedura začíná odesláním zprávy LAU Request uživatelským zařízením na náhodný přístupový kanál ([RACH](/mobilnisite/slovnik/rach/)), která obsahuje jeho dočasnou identitu mobilního účastníka ([TMSI](/mobilnisite/slovnik/tmsi/)) a starou identitu polohové oblasti ([LAI](/mobilnisite/slovnik/lai/)). Tato zpráva je směrována k novému VLR/MSC obsluhujícímu novou LA. Nový VLR následně kontaktuje starý VLR (pomocí staré LAI) nebo domovský lokální registr ([HLR](/mobilnisite/slovnik/hlr/)) za účelem autentizace účastníka a získání jeho profilu. Po úspěšné autentizaci a ověření nový VLR aktualizuje svou databázi, přidělí nové TMSI z důvodu ochrany soukromí a odešle uživatelskému zařízení zprávu LAU Accept, která obsahuje nové TMSI, pokud došlo k jeho přealokaci.

Klíčovými komponentami jsou uživatelské zařízení (UE), subsystém základnové stanice ([BSS](/mobilnisite/slovnik/bss/)) nebo subsystém rádiové sítě (RNS), MSC/VLR a HLR. LAU zajišťuje, že jsou informace o poloze uživatelského zařízení v síti přesné, aniž by vyžadovala neustálou signalizaci. Vyvažuje potřebu lokalizovat uživatelské zařízení pro příchozí hovory s ohledem na signalizační zátěž a spotřebu baterie zařízení. Periodické časovače LAU také vynucují aktualizace, i když je uživatelské zařízení nehybné, což zajišťuje, že síť neuchovává zastaralá polohová data.

## K čemu slouží

Procedura LAU byla vytvořena, aby vyřešila kritický problém lokalizace mobilního účastníka v rozsáhlé síti bez nutnosti nepřetržité, energeticky náročné signalizace. V raných mobilních systémech síť potřebovala metodu pro sledování přibližné polohy uživatele, aby mohla efektivně doručovat hovory. Účelem LAU je poskytnout kompromis mezi přesným sledováním polohy v reálném čase a úsporou zdrojů sítě a zařízení.

Řeší omezení plynoucí z absence jakéhokoli sledování polohy, což by si vyžádalo vyvolávání v celé síti pro každý příchozí hovor – což je vysoce neefektivní využití rádiových zdrojů. Seskupením buněk do polohových oblastí síť potřebuje znát pouze aktuální LA uživatelského zařízení. Uživatelské zařízení aktualizuje síť pouze při překročení hranice LA, což výrazně snižuje signalizační režii ve srovnání s aktualizacemi na úrovni buňky. Tento návrh je zásadní pro škálovatelnost a životnost baterie.

Historicky byla LAU základním kamenem správy mobility v GSM a umožnila roaming v rámci celé země i mezinárodně. Její vznik byl motivován potřebou automatizované, pro účastníka transparentní metody, která by udržovala síťová polohová data aktuální. Řeší problémy selhání doručení hovoru a nadměrného vyvolávacího provozu a tvoří základ pro správu mobility, která se vyvinula v aktualizaci směrovací oblasti (Routing Area Update) pro GPRS a aktualizaci sledované oblasti (Tracking Area Update) pro LTE/5G.

## Klíčové vlastnosti

- Aktualizuje síť o aktuální identitě polohové oblasti (LA) uživatelského zařízení.
- Spuštěna překročením hranic LA nebo periodickými časovači.
- Zahrnuje autentizaci účastníka a případné přealokování TMSI.
- Umožňuje efektivní vyvolávání (paging) jeho omezením na buňky v rámci poslední známé LA.
- Snižuje signalizační režii ve srovnání se sledováním na úrovni buňky.
- Nezbytná pro správu mobility a úspěšné doručení hovorů iniciovaných sítí.

## Související pojmy

- [RAI – Routing Area Identity](/mobilnisite/slovnik/rai/)
- [TAI – Tracking Area Identifier](/mobilnisite/slovnik/tai/)
- [TMSI – Temporary Mobile Subscriber Identifier](/mobilnisite/slovnik/tmsi/)
- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 25.967** (Rel-19) — Home NodeB RF Requirements Technical Report
- **TS 33.859** (Rel-11) — UTRAN Key Hierarchy Enhancement Study

---

📖 **Anglický originál a plná specifikace:** [LAU na 3GPP Explorer](https://3gpp-explorer.com/glossary/lau/)
