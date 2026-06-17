---
slug: "gal"
url: "/mobilnisite/slovnik/gal/"
type: "slovnik"
title: "GAL – Global Analysis Laboratory"
date: 2025-01-01
abbr: "GAL"
fullName: "Global Analysis Laboratory"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gal/"
summary: "GAL (Global Analysis Laboratory) je 3GPP rámec pro standardizované testování a analýzu služeb multimediální telefonie a kodeků. Prostřednictvím důsledného testování shody zajišťuje interoperabilitu a"
---

GAL je 3GPP rámec pro standardizované testování a analýzu služeb multimediální telefonie a kodeků, jehož cílem je zajistit interoperabilitu a kvalitu pro certifikaci sítí IMS.

## Popis

Global Analysis Laboratory (GAL) je komplexní rámec pro testování a analýzu definovaný 3GPP pro hodnocení služeb multimediální telefonie, se zvláštním zaměřením na výkon hlasových a video kodeků, kvalitu uživatelského prožitku (QoE) a interoperabilitu. Architektura GAL se skládá ze standardizovaných testovacích prostředí, měřicích metodik a analytických nástrojů, které umožňují konzistentní vyhodnocení multimediálních služeb napříč různými implementacemi a síťovými podmínkami. Mezi klíčové komponenty patří architektura testovacího systému s emulovanými síťovými prvky, standardizované testovací sekvence a scénáře, algoritmy pro objektivní měření kvality (jako POLQA pro hlas a VMAF pro video) a podrobné rámce pro reportování, které zachycují jak technické metriky, tak hodnocení percepční kvality.

GAL funguje prostřednictvím pečlivě řízených testovacích postupů, které simulují reálné síťové podmínky včetně různých vzorců ztráty paketů, scénářů s kolísáním zpoždění (jitter), profilů zpoždění a omezení šířky pásma. Testovací sekvence typicky zahrnují přehrání standardizovaných mediálních klipů testovaným systémem, zachycení výstupu a jeho porovnání s referenčními signály pomocí objektivních algoritmů a v případě potřeby i subjektivního hodnocení lidmi. Laboratorní prostředí zahrnuje emulátory sítí, které dokážou replikovat specifické podmínky rádiového přístupu (jako charakteristiky LTE, 5G NR nebo Wi-Fi), degradace v jádrové síti a problémy v transportní síti, které mohou ovlivnit kvalitu médií. Automatizované testovací nástroje řídí celý proces, od konfigurace systému přes provedení testu až po sběr a analýzu výsledků.

Z hlediska síťové integrace probíhá testování GAL v několika fázích vývoje produktu a certifikace. Výrobci zařízení používají metodiky GAL během vývoje, aby zajistili shodu s požadavky 3GPP, zatímco síťoví operátoři využívají podobné přístupy pro akceptační testování síťového vybavení a služeb. Rámec definuje specifické testovací případy pro různé scénáře, včetně hlasových hovorů, videohovorů, multimediálních zpráv a komunikace pro služby tísňového volání. Role GAL přesahuje rámec jednoduchého testování vyhověl/nevyhověl a zahrnuje podrobnou charakterizaci výkonu, která pomáhá identifikovat optimální pracovní body, odolnost za nepříznivých podmínek a interoperabilitu s dalšími implementacemi vyhovujícími standardům. Laboratorní prostředí podporuje jak samostatné testování jednotlivých komponent, tak integrované testování kompletních systémů včetně zařízení, síťového vybavení a aplikačních serverů.

## K čemu slouží

GAL byl vytvořen, aby řešil rostoucí složitost a variabilitu kvality multimediálních služeb v sítích 3GPP, zejména s přechodem na služby založené na IP Multimedia Subsystem (IMS). Když se hlasové a video služby přesouvaly z přepojování okruhů na přepojování paketů, tradiční testovací metody se ukázaly jako nedostatečné pro posouzení percepční kvality, kterou zažívají koncoví uživatelé. Průmysl potřeboval standardizované přístupy k vyhodnocení výkonu kodeků, odolnosti sítě a interoperability napříč zařízeními různých dodavatelů a různými síťovými podmínkami.

Mezi hlavní problémy, které GAL řeší, patří nekonzistentní kvalita uživatelského prožitku napříč sítěmi a zařízeními, problémy s interoperabilitou mezi různými implementacemi stejných standardů a nedostatek objektivních metrik pro porovnávání výkonu multimediálních služeb. Před GAL používali výrobci a operátoři proprietární testovací metodiky, které ztěžovaly přímá srovnání a často nedokázaly předpovědět výkon v reálném provozu. To vedlo k suboptimálnímu uživatelskému zážitku, zejména u služeb jako VoLTE a ViLTE, které vyžadují konzistentně vysokou kvalitu, aby mohly konkurovat over-the-top alternativám. GAL poskytuje společný rámec potřebný k zajištění, že multimediální služby splňují minimální kvalitativní prahové hodnoty bez ohledu na to, jaké vybavení od kterého dodavatele je nasazeno.

Historicky se GAL objevil souběžně s vývojem IMS a přechodem na plně IP sítě ve 3GPP Release 8. Když se průmysl posouval směrem ke službám rich communication services (RCS) a k vysokokvalitnímu hlasu a videu, došlo k uznání, že tradiční měření chybovosti bitů a rámců jsou pro hodnocení percepční kvality nedostatečná. GAL tuto mezeru zaplnil začleněním moderních algoritmů pro hodnocení kvality a vytvořením reprodukovatelných testovacích prostředí, která mohla ověřit jak technickou shodu, tak uživatelský prožitek. Rámec se dále vyvíjí, aby řešil nové výzvy včetně ultra vysokého rozlišení videa, imerzivního audia, komunikace s nízkou latencí a služeb poskytovaných přes 5G sítě s jejich jedinečnými charakteristikami, jako je síťové dělení (network slicing) a edge computing.

## Klíčové vlastnosti

- Standardizovaná testovací prostředí pro reprodukovatelné hodnocení kvality
- Algoritmy pro objektivní měření kvality (POLQA, VMAF, PESQ)
- Emulace síťových podmínek pro realistické testovací scénáře
- Komplexní testovací sekvence pokrývající různé typy služeb
- Rámce pro automatizované provádění testů a reportování výsledků
- Testování interoperability napříč implementacemi více dodavatelů

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)

## Definující specifikace

- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TR 26.952** (Rel-19) — EVS Codec Selection, Verification & Characterization
- **TR 26.997** (Rel-19) — IVAS Codec Specification

---

📖 **Anglický originál a plná specifikace:** [GAL na 3GPP Explorer](https://3gpp-explorer.com/glossary/gal/)
