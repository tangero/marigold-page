---
slug: "lspf"
url: "/mobilnisite/slovnik/lspf/"
type: "slovnik"
title: "LSPF – Location Subscriber Privacy Function"
date: 2025-01-01
abbr: "LSPF"
fullName: "Location Subscriber Privacy Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lspf/"
summary: "Síťová funkce, která vynucuje pravidla ochrany soukromí pro služby založené na poloze. Funguje jako bod rozhodování o politice (policy decision point), který kontroluje, zda je žádost o polohu (např."
---

LSPF je síťová funkce, která vynucuje pravidla ochrany soukromí účastníka tím, že autorizuje žádosti o polohu podle jeho profilu ochrany soukromí, a chrání tak jeho polohová data.

## Popis

Location Subscriber Privacy Function (LSPF) je klíčová logická komponenta v architektuře služeb určování polohy ([LCS](/mobilnisite/slovnik/lcs/)) podle 3GPP, která se konkrétně nachází v jádru sítě. Jejím primárním úkolem je fungovat jako strážce a bod vynucování pravidel (policy enforcement point) pro všechny žádosti o polohu cílené na mobilního účastníka. Když klient služby určování polohy (LCS Client) – což může být externí aplikace, poskytovatel přidružených služeb nebo interní síťová entita – požádá o geografickou polohu mobilní stanice ([MS](/mobilnisite/slovnik/ms/)), je žádost směrována přes Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)). GMLC vyvolá LSPF, aby provedla kontrolu autorizace z hlediska ochrany soukromí, než začne jakýkoli proces určování polohy.

Z architektonického hlediska LSPF komunikuje s Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) účastníka, aby získala jeho profil ochrany soukromí pro polohu. Tento profil je konfigurován účastníkem, často prostřednictvím jeho poskytovatele služeb, a definuje pravidla pro zveřejňování polohy. Profil typicky zahrnuje nastavení, jako například kteří konkrétní LCS Clienti smějí žádat o polohu, časová okna, ve kterých jsou žádosti povoleny, a zda je vyžadováno upozornění nebo ověření vůči účastníkovi. LSPF vyhodnocuje příchozí žádost vůči tomuto uloženému profilu. Kontrola zahrnuje ověření identity klienta, typu žádosti o polohu (např. okamžitá nebo odložená) a požadované kvality služby (např. přesnost).

Pokud LSPF žádost autorizuje, vrátí GMLC kladnou odpověď, který pak pokračuje v interakci s obsluhujícím Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) nebo Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)), aby zahájil proces určování polohy s rádiovou přístupovou sítí. Pokud je žádost na základě pravidel ochrany soukromí zamítnuta, LSPF vrátí GMLC zamítavou odpověď, který pak pošle chybovou odpověď LCS Clientovi a žádné informace o poloze nejsou zveřejněny. V případech, kdy profil účastníka vyžaduje upozornění nebo ověření, může logika LSPF spustit interakci s účastníkem, například prostřednictvím SMS s žádostí o souhlas, než bude pokračováno. Tato funkce je zásadní pro dodržování regulatorních požadavků na ochranu soukromí uživatelů a pro budování důvěry účastníků ve služby založené na poloze.

## K čemu slouží

LSPF byla vytvořena, aby řešila významné obavy o ochranu soukromí vyplývající ze schopnosti určit geografickou polohu mobilního uživatele. Jak se mobilní sítě vyvíjely od poskytování jednoduché hlasové služby k umožnění pokročilých datových služeb a služeb založených na poloze (LBS), potenciál pro zneužití polohových dat se stal závažným problémem. Bez přísných kontrol by jakákoli autorizovaná nebo neautorizovaná entita mohla sledovat pohyby uživatele, což by vedlo k závažným porušením soukromí. LSPF poskytuje standardizovaný, na síti založený mechanismus, který tomu má zabránit.

Její vývoj byl motivován jak regulatorním tlakem, tak komerční potřebou učinit LBS přijatelné pro spotřebitele. Předpisy v mnoha regionech ukládají, že uživatelé musí mít kontrolu nad tím, kdo může přistupovat k jejich polohovým datům. Technicky dřívější přístupy postrádaly centralizovanou, na účastníka zaměřenou funkci pro správu pravidel. LSPF to řeší oddělením logiky pravidel ochrany soukromí od mechanismu výpočtu polohy (např. GMLC nebo polohového uzlu). Vytváří jasné, standardizované rozhraní pro kontrolu ochrany soukromí, které umožňuje flexibilní a spravovatelné profily ochrany soukromí.

Poskytnutím této funkce 3GPP umožnila bezpečné nasazení hodnotných služeb, jako je tísňové volání (E911/112), správa vozových parků, reklama založená na poloze nebo aplikace pro vyhledání přátel. Dává účastníkům jistotu, že jejich poloha nebude zveřejněna bez jejich vědomí nebo souhlasu, což byl základní předpoklad pro široké přijetí LBS. LSPF tedy není jen technickou funkcí, ale základním kamenem etického a právního rámce pro provoz mobilních sítí.

## Klíčové vlastnosti

- Centralizovaná autorizace z hlediska ochrany soukromí pro všechny žádosti o službu určování polohy.
- Dotazuje se na profily ochrany soukromí účastníků uložené v HLR/HSS.
- Podporuje konfigurovatelná pravidla založená na identifikátoru LCS Clienta, denní době a typu služby.
- Spravuje procedury upozornění a ověření vůči účastníkovi.
- Integruje se s Gateway Mobile Location Centre (GMLC) v architektuře LCS.
- Poskytuje standardizované chybové odpovědi pro neautorizované žádosti.

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [LSPF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lspf/)
