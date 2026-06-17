---
slug: "lab"
url: "/mobilnisite/slovnik/lab/"
type: "slovnik"
title: "LAB – Listening LABoratory"
date: 2025-01-01
abbr: "LAB"
fullName: "Listening LABoratory"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lab/"
summary: "Standardizované testovací prostředí definované organizací 3GPP pro hodnocení výkonu řečových a zvukových kodeků za kontrolovaných podmínek. Poskytuje rámec pro reprodukovatelné, objektivní hodnocení k"
---

LAB je standardizované 3GPP testovací prostředí pro hodnocení výkonu řečových a zvukových kodeků za kontrolovaných podmínek, které zajišťuje reprodukovatelné posouzení kvality a konzistentní uživatelský zážitek.

## Popis

Listening LABoratory (LAB) je formalizovaná testovací metodologie a prostředí specifikované v 3GPP TS 26.935. Jejím hlavním účelem je posoudit subjektivní kvalitu řečových a zvukových kodeků používaných v mobilních komunikacích. LAB není fyzické síťové zařízení, ale přísný procedurální rámec. Definuje celý řetězec pro hodnocení kvality, včetně výběru expertních posluchačů, vytváření testovacích sekvencí pomocí standardizovaného zdrojového materiálu, specifických podmínek pro přehrávání a poslech a statistických metod pro analýzu hodnocení posluchačů. Tento proces generuje Mean Opinion Score ([MOS](/mobilnisite/slovnik/mos/)), což je klíčová metrika pro výkon kodeku.

Architektura LAB je založena na kontrolovaném akustickém prostředí. Posluchači jsou umístěni v odhlučněných kabinách s kalibrovanou zvukovou technikou, aby byl eliminován vnější hluk a zajištěna konzistentní úroveň přehrávání. Testovací sekvence jsou pečlivě připraveny tak, aby reprezentovaly širokou škálu akustických podmínek a zahrnovaly zpracovanou řeč (prostřednictvím testovaného kodeku) spolu se skrytými referenčními signály. Základní metodologie spočívá v prezentaci těchto sekvencí panelu posluchačů, kteří ohodnotí vnímanou kvalitu na standardizované škále. Výsledná hodnocení jsou následně zpracována pomocí specifických statistických technik uvedených ve specifikaci, aby vznikly spolehlivé a srovnatelné hodnoty MOS.

Role LAB v ekosystému 3GPP je zásadní pro standardizaci kodeků. Předtím, než je nový řečový nebo zvukový kodek (jako [AMR](/mobilnisite/slovnik/amr/), [EVS](/mobilnisite/slovnik/evs/) nebo [AMR-WB](/mobilnisite/slovnik/amr-wb/)) schválen pro zařazení do specifikací, musí projít přísným testováním v LAB, aby prokázal, že splňuje minimální prahové hodnoty kvality a přináší zlepšení oproti stávajícím kodekům. Tím se zajišťuje, že technologický pokrok v kompresi a efektivitě využití šířky pásma neprobíhá na úkor nepřijatelné zvukové kvality pro koncového uživatele. LAB poskytuje objektivní, reprodukovatelné důkazy potřebné pro tato standardizační rozhodnutí.

## K čemu slouží

LAB byl vytvořen k vyřešení základního problému, jak objektivně a spolehlivě měřit subjektivní zážitek z kvality řeči v digitálních mobilních sítích. Rané digitální kodeky zaváděly artefakty, jako je kvantizační šum a omezení šířky pásma, které bylo obtížné kvantifikovat pomocí jednoduchých elektrických měření. Účelem LAB je poskytnout standardizovanou, vědeckou metodu pro převod lidského vnímání na kvantifikovatelnou metriku ([MOS](/mobilnisite/slovnik/mos/)), což umožňuje spravedlivé srovnání různých kodekových algoritmů a implementací.

Historicky, bez standardizované metody poslechových testů, nemohli vývojáři kodeků a provozovatelé sítí spolehlivě porovnávat výsledky z různých testovacích zařízení. To činilo proces výběru a standardizace kodeků subjektivním a potenciálně zkresleným. Specifikace LAB tento problém řeší definicí všech kontrolovatelných proměnných – od fyzického poslechového prostředí a výběru posluchačů až po testovací materiál a statistickou analýzu – čímž zajišťuje, že výsledky jsou reprodukovatelné a srovnatelné mezi různými laboratořemi po celém světě. Byla motivována potřebou společného 'jazyka' pro hodnocení kvality, který by poháněl vývoj řečových kodeků od plné rychlosti GSM (Full Rate) po dnešní Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) a dále, vždy s ověřeným uživatelsky orientovaným měřítkem kvality.

## Klíčové vlastnosti

- Standardizovaná testovací metodologie pro subjektivní hodnocení kvality řeči a zvuku
- Definice kontrolovaného akustického prostředí a kritérií pro výběr posluchačů
- Postup pro generování a prezentaci testovacích sekvencí včetně zpracovaných a referenčních signálů
- Statistické zpracování hodnocení posluchačů pro výpočet Mean Opinion Score (MOS)
- Zajišťuje reprodukovatelnost a srovnatelnost testovacích výsledků mezi různými laboratořemi
- Poskytuje základní důkazy o kvalitě vyžadované pro standardizaci kodeků v 3GPP

## Definující specifikace

- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia

---

📖 **Anglický originál a plná specifikace:** [LAB na 3GPP Explorer](https://3gpp-explorer.com/glossary/lab/)
