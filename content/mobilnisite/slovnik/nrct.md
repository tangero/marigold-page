---
slug: "nrct"
url: "/mobilnisite/slovnik/nrct/"
type: "slovnik"
title: "NRCT – No Reply Call Timer"
date: 2025-01-01
abbr: "NRCT"
fullName: "No Reply Call Timer"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nrct/"
summary: "Časovač NRCT (No Reply Call Timer) je časovač používaný v mobilních sítích s přepojováním okruhů pro řízení sestavování hovoru, když volaná strana neodpoví. Určuje, jak dlouho bude síť čekat na odpově"
---

NRCT je časovač v mobilních sítích s přepojováním okruhů, který určuje, jak dlouho čekat na odpověď volané strany, než je pokus o spojení zrušen.

## Popis

Časovač NRCT (No Reply Call Timer) je časovač v jádře sítě definovaný ve specifikacích 3GPP, primárně v rámci procedur řízení hovoru s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)). V síti jej spravuje Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo MSC Server. Při zahájení příchozího hovoru do mobilní sítě MSC vyvolá volaného účastníka a po obdržení odezvy zřídí hlasovou cestu k mobilní stanici volané strany. Časovač NRCT se spustí, když je hovor předán volané straně (tj. když telefon začne zvonit). Jeho základní úlohou je dohlížet na fázi sestavování hovoru a čekat na odpověď volané strany. Pokud volaná strana odpoví před vypršením časovače, časovač se zastaví a hovor probíhá normálně. Pokud časovač vyprší před obdržením odpovědi, MSC to vyhodnotí jako stav 'žádná odpověď' a zahájí procedury uvolnění hovoru.

Z architektonického hlediska je NRCT konfigurovatelný parametr v rámci logiky zpracování hovorů MSC. Interaguje s dalšími časovači a funkcemi řízení hovoru, například těmi, které spravují vyzvánění a spojení. Po vypršení NRCT MSC následuje předdefinované procedury, které typicky zahrnují zrušení sestavování hovoru směrem k volající straně a případně aktivaci doplňkových služeb. Klíčovou interakcí je provázání s doplňkovou službou Přesměrování hovoru při neodpovědi (CFNRy). Pokud má volaný účastník tuto službu aktivovanou, MSC po vypršení NRCT hovor nejen jednoduše zruší. Místo toho se pokusí hovor přesměrovat na předdefinované číslo, například na systém hlasové schránky nebo na jiné telefonní číslo. Hodnota NRCT tedy přímo definuje dobu vyzvánění, kterou volající zažije, než je hovor přesměrován.

Činnost časovače je podrobně popsána v diagramech průběhu hovoru ve specifikacích jako 23.018. Je součástí základního modelu stavu hovoru ([BCSM](/mobilnisite/slovnik/bcsm/)) pro hovory iniciované z mobilní sítě i do mobilní sítě. Hodnota NRCT je konfigurovatelná operátorem a může se lišit v závislosti na síťové politice, regionálních předpisech nebo profilech služeb konkrétního účastníka. Zatímco jeho primární doménou je starší jádro sítě s přepojováním okruhů (CS-CN) pro hlasové hovory, koncept přetrvává v IP Multimedia Subsystem (IMS) pro VoIP hovory, byť je často implementován pomocí jiných, pro IMS specifických časovačů (jako jsou Session Timers). V moderních sítích s útlumem CS sítí a nástupem VoLTE a VoNR je explicitní parametr NRCT méně výrazný, ale funkční požadavek – řízení doby nevyzvednutého hovoru – zůstává klíčový v rámci funkcí řízení IMS relací.

## K čemu slouží

NRCT byl vytvořen k řešení základního problému v automatizované telefonii: řízení zdrojů a zajištění předvídatelného uživatelského zážitku, když volaná strana neodpoví. Bez takového časovače by se pokus o hovor teoreticky mohl donekonečna udržovat ve stavu 'vyzvánění', blokuje přitom cenné síťové zdroje (např. rádiové kanály, okruhy na trunkech a kapacitu ústředny) bez užitečného výsledku. To by vedlo k vyčerpání zdrojů a neefektivitě sítě. NRCT poskytuje čistý, časově omezený mechanismus pro selhání procedury sestavení hovoru.

Historicky byl tento časovač standardní součástí telekomunikačních ústředen již od předcelulární éry. 3GPP jej standardizovalo pro GSM a UMTS sítě s přepojováním okruhů, aby zajistilo konzistentní chování napříč zařízeními různých výrobců a operátorů. Umožňuje implementaci přidaných služeb, jako je Přesměrování hovoru při neodpovědi (CFNRy), což zlepšuje uživatelský zážitek tím, že zajišťuje, aby hovory nebyly pouze zmeškány. Konfigurovatelná povaha časovače umožňuje operátorům přizpůsobit dobu vyzvánění; kratší časovač může snížit zatížení sítě, ale frustruje uživatele, kteří potřebují více času na odpověď, zatímco delší časovač zvyšuje pravděpodobnost vyzvednutí, ale déle využívá zdroje. NRCT tedy představuje klasický inženýrský kompromis mezi využitím zdrojů a kvalitou služby, standardizovaný pro zajištění interoperability v globálním mobilním systému s více výrobci a operátory.

## Klíčové vlastnosti

- Časovač spravovaný MSC/MSC Server během sestavování příchozího hovoru do mobilní sítě.
- Dohlíží na fázi vyzvánění, startuje při začátku vyzvánění telefonu volané strany.
- Po vypršení spustí uvolnění hovoru nebo aktivaci služby Přesměrování hovoru při neodpovědi (CFNRy).
- Konfigurovatelná hodnota (typicky v rozsahu 15-30 sekund).
- Integrální součást základního modelu stavu hovoru (BCSM) pro sítě s přepojováním okruhů.
- Zajišťuje efektivní uvolnění síťových zdrojů u nevyzvednutých hovorů.

## Definující specifikace

- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain

---

📖 **Anglický originál a plná specifikace:** [NRCT na 3GPP Explorer](https://3gpp-explorer.com/glossary/nrct/)
