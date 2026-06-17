---
slug: "lsof"
url: "/mobilnisite/slovnik/lsof/"
type: "slovnik"
title: "LSOF – Location System Operations Function"
date: 2025-01-01
abbr: "LSOF"
fullName: "Location System Operations Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lsof/"
summary: "Funkční entita definovaná v raných specifikacích 3GPP, která poskytuje základní schopnosti pro služby určování polohy. Spravuje žádosti o polohu, získává měření pro určování polohy, vypočítává polohu"
---

LSOF je funkční entita v 3GPP, která poskytuje základní služby určování polohy tím, že spravuje žádosti o polohu, získává měření, vypočítává polohu UE a doručuje výsledek.

## Popis

Location System Operations Function (LSOF) je základní síťová architektonická komponenta definovaná v raných vydáních 3GPP (před Release 4) pro poskytování Location Services ([LCS](/mobilnisite/slovnik/lcs/)). Představuje centrální funkční entitu zodpovědnou za orchestraci celého procesu určování geografické polohy User Equipment (UE). LSOF komunikuje s dalšími síťovými elementy, jako je Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)), Serving Mobile Location Centre (SMLC) a samotné UE, aby vyřídila žádosti o polohu od externích LCS klientů nebo interních síťových aplikací. Její operace zahrnují autorizaci, koordinaci metody určování polohy, výpočet polohy a doručení výsledku.

Z architektonického hlediska byly odpovědnosti LSOF v pozdějších vydáních často distribuovány mezi konkrétní uzly, ale původně zahrnovala klíčové procedury. Po přijetí žádosti o polohu (prostřednictvím GMLC) LSOF nejprve provedla ověření soukromí a autorizační kontroly, aby zajistila, že žádající klient má oprávnění lokalizovat cílové UE. Poté zahájila relaci určování polohy kontaktováním příslušných síťových elementů obsluhujících aktuální oblast UE. To zahrnovalo interakci se SMLC (nebo podobnou funkcionalitou v RAN), která je zodpovědná za výběr metody určování polohy (např. Cell-ID, [OTDOA](/mobilnisite/slovnik/otdoa/), U-TDOA, Assisted-GNSS) a získání potřebných rádiových měření z UE a/nebo základnových stanic.

LSOF přijímala tato surová nebo částečně zpracovaná měření od SMLC. Pomocí těchto dat spolu se znalostí souřadnic základnových stanic a dalších kalibračních informací LSOF provedla nebo dohlížela na finální výpočet polohy, převádějíc měření na geografický odhad (zeměpisná šířka, délka a nejistota). Nakonec výsledek naformátovala podle požadovaných parametrů Quality of Service (QoS) – jako je přesnost a doba odezvy – specifikovaných v původní žádosti, a doručila výsledek zpět LCS klientovi prostřednictvím GMLC. LSOF tedy fungovala jako mozek služby určování polohy, řídila pracovní postup, zajišťovala zabezpečení/soukromí a garantovala doručení použitelného údaje o poloze.

## K čemu slouží

LSOF byla konceptualizována, aby poskytla standardizovaný, síťový rámec pro služby určování polohy v sítích 2G a raných 3G. Před její definicí byly možnosti určování polohy proprietární a fragmentované, což bránilo vývoji interoperabilních služeb, jako je lokalizace pro tísňová volání (E911), tarifování na základě polohy, správa vozových parků a aplikace typu "najdi můj telefon". Hlavní problém, který řešila, byla definice jasného funkčního modelu a souboru rozhraní (např. mezi LSOF, [GMLC](/mobilnisite/slovnik/gmlc/) a SMLC), který umožnil konzistentní implementaci [LCS](/mobilnisite/slovnik/lcs/) napříč různými zařízeními od výrobců a síťovými operátory.

K jejímu vytvoření významně přispěly regulatorní požadavky, zejména pro tísňové služby, které vyžadovaly spolehlivý mechanismus, aby síťoví operátoři mohli poskytnout polohu volajícího Public Safety Answering Points (PSAPs). LSOF poskytla základní operační logiku pro splnění těchto zákonných požadavků. Dále umožnila komerční služby založené na poloze tím, že nabídla jediný, řiditelný kontrolní bod pro autentizaci, účtování a servisní logiku, oddělující servisní vrstvu od specifik podkladové rádiové přístupové technologie.

Jak se architektury 3GPP vyvíjely od Release 4 dále, funkce popsané LSOF byly konkrétněji přiděleny specifickým síťovým uzlům, jako je GMLC (pro obsluhu klienta a soukromí), SMLC (pro řízení určování polohy) a [E-SMLC](/mobilnisite/slovnik/e-smlc/) v LTE. Termín 'LSOF' je tedy převážně historický a fundamentální, představující konceptuální plán, ze kterého byla postavena moderní, distribuovaná architektura LCS. Stanovila základní operace, které musí jakýkoli systém služby určování polohy provádět, a zajistila, že služby mohou být vyvíjeny na stabilním, standardizovaném základě.

## Klíčové vlastnosti

- Řídí end-to-end proceduru žádosti o polohu od zahájení po doručení výsledku.
- Provádí ověření soukromí a autorizaci pro žádosti o polohu.
- Koordinuje s RAN elementy (SMLC) pro výběr a provedení metod určování polohy.
- Vypočítává finální odhad geografické polohy ze surových měření sítě/UE.
- Formátuje a doručuje výsledky polohy podle požadovaných parametrů QoS.
- Sloužila jako základní funkční model pro standardizované 3GPP Location Services.

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [LSOF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lsof/)
