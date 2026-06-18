---
slug: "mpu"
url: "/mobilnisite/slovnik/mpu/"
type: "slovnik"
title: "MPU – Media Processing Unit"
date: 2025-01-01
abbr: "MPU"
fullName: "Media Processing Unit"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mpu/"
summary: "Funkční jednotka v rámci mediálního serveru nebo funkce mediálních zdrojů (Media Resource Function), která provádí zpracování mediálních datových proudů v reálném čase, jako je transkódování, změna da"
---

MPU je funkční jednotka v rámci mediálního serveru, která provádí zpracování mediálních datových proudů v reálném čase, jako je transkódování a mixování, za účelem přizpůsobení obsahu uživatelskému zařízení a podmínkám sítě v sítích IMS a 5G.

## Popis

Mediální procesní jednotka (MPU) je logická nebo fyzická procesní entita odpovědná za manipulaci s mediálními datovými proudy v reálném čase v rámci telekomunikační sítě. Je klíčovou součástí funkcí mediálních zdrojů ([MRF](/mobilnisite/slovnik/mrf/)), které jsou součástí IP multimediální podsystému (IMS) a mediální architektury 5G. MPU provádí výpočetně náročné úlohy zpracování médií na zvukových, video nebo textových proudech. Její činnost zahrnuje příjem mediálních paketů prostřednictvím protokolu [RTP](/mobilnisite/slovnik/rtp/) (Real-time Transport Protocol), jejich zpracování podle servisní logiky a následné předávání upravených proudů. Zpracování je řízeno řadičem funkce mediálních zdrojů ([MRFC](/mobilnisite/slovnik/mrfc/)) nebo aplikačním serverem ([AS](/mobilnisite/slovnik/as/)) za použití protokolů jako H.248 (Megaco) nebo Media Server Markup Language (MSML).

Z architektonického hlediska může být MPU implementována jako dedikovaný hardware, softwarová instance na serveru s obecným účelem nebo ve virtualizovaném/cloud-nativním prostředí jako součást mediální funkce ([MF](/mobilnisite/slovnik/mf/)) v 5G. Mezi klíčové vnitřní komponenty patří kodeky pro kódování a dekódování, digitální signálové procesory ([DSP](/mobilnisite/slovnik/dsp/)) pro manipulaci se zvukem a grafické procesorové jednotky ([GPU](/mobilnisite/slovnik/gpu/)) pro zpracování videa. MPU vykonává funkce jako transkódování (převod média z jednoho kodeku na jiný, např. z [AMR](/mobilnisite/slovnik/amr/) na Opus), změna datového toku (transrating), změna rozlišení videa (transsizing), mixování (pro konference více účastníků), generování/detekce tónů a převod řeči na text. Například v konferenčním hovoru by MPU přijímala více zvukových proudů, mixovala je do jednoho složeného proudu pro každého účastníka a případně jej transkódovala na kodek, který zařízení účastníka podporuje.

V systémech 5G jsou schopnosti zpracování médií stále více dekomponovány a distribuovány. Koncept MPU odpovídá funkci zpracování médií (MPF) nebo obecným prostředkům pro zpracování médií, které může orchestrovat 5G páteřní síť. Funkce správy relací (SMF) a funkce řízení politik (PCF) mohou ovlivnit výběr a alokaci prostředků MPU na základě požadované QoS a parametrů služby. Role MPU je klíčová pro adaptaci služeb; zajišťuje, že mediální obsah je doručován ve formátu vhodném pro zobrazovací zařízení příjemce, jeho výpočetní výkon a síťovou šířku pásma, čímž optimalizuje uživatelský zážitek a efektivitu sítě.

## K čemu slouží

MPU existuje za účelem odlehčení komplexních úloh zpracování médií od koncových bodů uživatelů a aplikačních serverů a centralizace těchto náročných operací v rámci sítě. Uživatelská zařízení, zejména v IoT nebo s omezenými schopnostmi, nemusí podporovat všechny mediální kodeky nebo mít dostatečný výpočetní výkon pro úlohy jako mixování více účastníků nebo překlad v reálném čase. MPU tento problém řeší tím, že poskytuje síťový, škálovatelný prostředek, který dokáže mediální proudy za běhu přizpůsobit schopnostem zařízení a aktuálním síťovým podmínkám, čímž zajišťuje interoperabilitu a konzistentní uživatelský zážitek.

Historicky, v sítích s přepojováním okruhů, byly podobné funkce prováděny konferenčními můstky a systémy IVR za použití specializovaného hardwaru. S přechodem na plně IP sítě a IMS vznikla potřeba standardizovaného, flexibilního prostředku pro zpracování médií, kterým by bylo možné dynamicky řídit širokou škálu služeb, jako je VoLTE, videokonference a interaktivní hlasová odpověď (IVR). Koncept MPU formalizuje tento prostředek v rámci specifikací 3GPP, což umožňuje interoperabilitu mezi zařízeními různých výrobců a poskytovatelům služeb nabízet pokročilé komunikační služby (RCS) a imerzivní mediální zážitky.

Motivace pro jeho specifikaci v 3GPP, zejména v kontextu 5G a edge computingu, je podpora aplikací s nízkou latencí, jako je rozšířená realita, cloudové hraní a průmyslové teleoperace. Nasazením MPU na okraji sítě se latence zpracování snižuje. Dále, při síťovém slicingu, mohou být vyhrazené prostředky MPU přiděleny řezu (slice) pro zaručení výkonu konkrétních služeb náročných na média. MPU tak řeší výzvy mediální heterogenity, distribuce výpočetní zátěže a zajištění kvality v moderních multimediálních komunikačních službách.

## Klíčové vlastnosti

- Transkódování médií v reálném čase mezi různými audio/video kodeky
- Mixování mediálních proudů pro konferenční hovory a vysílací služby
- Přizpůsobení datového toku a rozlišení médií (transrating/transsizing)
- Podpora analýzy médií (např. rozpoznávání řeči, analýza sentimentu)
- Dynamická alokace a řízení prostředků prostřednictvím standardizovaných protokolů (např. H.248)
- Virtualizované nasazení podporující cloud-nativní a edge computing architektury

## Definující specifikace

- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP

---

📖 **Anglický originál a plná specifikace:** [MPU na 3GPP Explorer](https://3gpp-explorer.com/glossary/mpu/)
