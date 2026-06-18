---
slug: "cq"
url: "/mobilnisite/slovnik/cq/"
type: "slovnik"
title: "CQ – Conversational Quality"
date: 2025-01-01
abbr: "CQ"
fullName: "Conversational Quality"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cq/"
summary: "CQ (Conversational Quality, kvalita konverzace) je standardizovaná metrika 3GPP pro hodnocení kvality hlasových a video hovorů v službách komunikace v reálném čase. Poskytuje objektivní měření kvality"
---

CQ je standardizovaná metrika 3GPP pro objektivní měření kvality hlasových a video hovorů v reálném čase, jak ji vnímá uživatel, za účelem monitorování a optimalizace výkonu sítě.

## Popis

Conversational Quality (CQ, kvalita konverzace) je komplexní rámec pro hodnocení kvality definovaný v 3GPP TS 26.935, který měří kvalitu konverzačních služeb od konce ke konci, primárně se zaměřením na hlasovou a video telefonii. Rámec využívá standardizované algoritmy a modely k predikci kvality, jak ji vnímá uživatel, na základě parametrů sítě a médií, čímž poskytuje objektivní alternativu k subjektivnímu testování lidmi. CQ funguje analýzou klíčových ukazatelů kvality v celé cestě hovoru, včetně výkonu kodeku, přenosových charakteristik a závad v síti, které ovlivňují konverzační zážitek.

Technická implementace CQ zahrnuje více měřicích bodů a zpracovatelských fází. Síťové prvky během aktivních hovorů sbírají surové metriky kvality, jako jsou míra ztráty paketů, rozkmity (jitter), zpoždění a zkreslení kodeku. Tyto metriky jsou zpracovány standardizovanými modely pro predikci kvality, které převádějí technické parametry na ekvivalenty středního známkového skóre ([MOS](/mobilnisite/slovnik/mos/)), což reprezentuje, jak by uživatelé ohodnotili kvalitu hovoru na standardizované škále. Rámec podporuje jak rušivé (aktivní testování), tak nerušivé (pasivní monitorování) přístupy k měření, což operátorům umožňuje implementovat monitorování kvality s různou mírou dopadu na síť.

Z architektonického hlediska se CQ integruje se systémy monitorování sítě prostřednictvím standardizovaných rozhraní a mechanismů reportování. Mezi klíčové komponenty patří body sběru měření na různých místech sítě (radiový přístup, páteřní síť, mediální brány), funkce pro výpočet kvality, které aplikují standardizované algoritmy, a reportovací systémy, které agregují a prezentují metriky kvality. Rámec zohledňuje jak kvalitu poslechu (jednosměrná kvalita zvoku/videa), tak kvalitu konverzace (interaktivní aspekty včetně zpoždění a ozvěn), a poskytuje tak komplexní pohled na výkon služby.

CQ hraje klíčovou roli v optimalizaci sítě a zajištění služeb tím, že umožňuje operátorům identifikovat vzorce degradace kvality, korelovat problémy s kvalitou se stavem sítě a implementovat cílená vylepšení. Standardizovaná povaha měření CQ umožňuje konzistentní srovnávání kvality napříč různými sítěmi, zařízeními a implementacemi služeb. Poskytováním objektivních a opakovatelných hodnocení kvality podporuje CQ plánování sítě založené na kvalitě, odstraňování problémů a strategie diferenciace služeb v mobilních sítích.

## K čemu slouží

Conversational Quality (CQ) byl vyvinut, aby řešil rostoucí potřebu standardizovaného, objektivního měření kvality v mobilních hlasových a video službách. Před standardizací CQ používali operátoři a výrobci zařízení proprietární přístupy k měření kvality, které ztěžovaly srovnání napříč sítěmi a bránily interoperabilitě. Nedostatek standardizovaných metrik kvality také komplikoval dodržování regulatorních požadavků a ověřování smluvních parametrů služeb ([SLA](/mobilnisite/slovnik/sla/)) v síťových prostředích s více dodavateli.

Vytvoření CQ bylo motivováno vývojem od okruhově spínaných k paketově spínaným hlasovým službám (VoIP) v sítích 3GPP, které přinesly nové výzvy v kvalitě související se ztrátou paketů, rozkmitem (jitter) a proměnným zpožděním. Tradiční přístupy k měření kvality navržené pro okruhově spínané sítě byly nedostatečné pro paketové služby, což si vyžádalo nové rámce pro měření, které by dokázaly zohlednit charakteristiky IP sítí. CQ poskytl standardizované řešení, které může fungovat napříč různými síťovými architekturami a implementacemi služeb.

CQ řeší základní problém zajištění kvality v konverzačních službách tím, že poskytuje konzistentní, objektivní rámec pro měření, který koreluje technické síťové parametry s kvalitou, jak ji vnímá uživatel. To operátorům umožňuje proaktivně spravovat kvalitu služeb, identifikovat degradaci dříve, než ovlivní velký počet uživatelů, a činit rozhodnutí o investicích a optimalizacích sítě na základě dat. Rámec také podporuje regulatorní požadavky na reportování kvality a pomáhá operátorům prokazovat kvalitu služeb zákazníkům a regulátorům.

## Klíčové vlastnosti

- Standardizované modely pro predikci kvality založené na doporučeních ITU-T
- Podpora jak rušivých (aktivní testování), tak nerušivých (pasivní monitorování) přístupů k měření
- Integrace se systémy správy sítě prostřednictvím standardizovaných reportovacích rozhraní
- Více-dimenzionální hodnocení kvality pokrývající kvalitu poslechu, kvalitu konverzace a synchronizaci médií
- Odhad kvality s ohledem na kodek, který zohledňuje specifické charakteristiky a závady kodeků
- Schopnosti měření kvality v reálném čase a následného zpracování

## Definující specifikace

- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia

---

📖 **Anglický originál a plná specifikace:** [CQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/cq/)
