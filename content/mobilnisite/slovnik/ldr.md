---
slug: "ldr"
url: "/mobilnisite/slovnik/ldr/"
type: "slovnik"
title: "LDR – Location Deferred Request"
date: 2026-01-01
abbr: "LDR"
fullName: "Location Deferred Request"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ldr/"
summary: "Location Deferred Request (LDR, požadavek na odložené určení polohy) je schopnost v rámci architektury služeb určování polohy (LCS), která umožňuje klientovi požadovat, aby byla poloha cílového UE urč"
---

LDR je schopnost služeb určování polohy, která umožňuje klientovi požadovat, aby byla poloha cílového zařízení určena a doručena v určeném pozdějším čase.

## Popis

Location Deferred Request (LDR, požadavek na odložené určení polohy) je funkce systému služeb určování polohy ([LCS](/mobilnisite/slovnik/lcs/)) dle 3GPP. Funguje v rámci standardizované architektury LCS, která zahrnuje klienta LCS, server LCS (typicky Gateway Mobile Location Centre - [GMLC](/mobilnisite/slovnik/gmlc/)) a uzly jádra sítě (např. [MSC](/mobilnisite/slovnik/msc/), SGSN, [MME](/mobilnisite/slovnik/mme/)), které komunikují s rádiovou přístupovou sítí a UE. Mechanismus LDR umožňuje autorizovanému klientovi LCS odeslat požadavek na určení polohy s podmínkou odloženého hlášení. Namísto okamžitého spuštění procedury určení polohy síť požadavek uloží a aktivuje jej při splnění specifikované podmínky. Mezi klíčové komponenty patří parametry odloženého požadavku na polohu uložené v síti (např. v GMLC nebo vyhrazeném servisním uzlu), časovače a spouštěcí události. Požadavek specifikuje kritéria, jako je jediný budoucí absolutní čas, periodický interval (např. každou hodinu) nebo událost změny oblasti (např. když UE vstoupí do definované geografické oblasti nebo ji opustí). Když dojde ke spouštěcí podmínce, síť provede standardní proceduru určení polohy, která může být síťová (např. pomocí časového předstihu nebo pozorovaného časového rozdílu příchodu), založená na UE (pomocí [GNSS](/mobilnisite/slovnik/gnss/) jako [GPS](/mobilnisite/slovnik/gps/)) nebo asistované/hybridní metody. Jakmile je poloha získána, síť doručí výsledek (např. zeměpisné souřadnice) žádajícímu klientovi LCS podle pokynů pro doručení uvedených v odloženém požadavku. Tento proces odděluje požadavek od okamžitého využití síťových prostředků a prostředků UE pro určování polohy, což umožňuje efektivnější plánování a šetrnější provoz vůči baterii UE, zejména pro neurgentní sledovací aplikace. Funkce závisí na schopnosti sítě spravovat a korelovat více odložených požadavků, řídit jejich životní cyklus (vytvoření, aktivace, provedení, zrušení) a zajišťovat ochranu soukromí a bezpečnost v souladu se souhlasem účastníka.

## K čemu slouží

Location Deferred Request byl vytvořen, aby rozšířil využitelnost služeb určování polohy v celulárních sítích mimo jednoduché, okamžité dotazy typu „kde jsi teď“. Rané schopnosti [LCS](/mobilnisite/slovnik/lcs/) byly primárně v reálném čase, což omezovalo aplikace na okamžitou navigaci, nouzové služby (E911) a podobné časově kritické případy použití. Mnoho komerčních a podnikových aplikací však vyžaduje informace o poloze na základě plánu nebo událostí bez neustálého aktivního dotazování. Příklady zahrnují správu vozového parku pro periodické zaznamenávání polohy, sledování aktiv pro případ krádeže (hlášení polohy pouze při pohybu), reklamu založenou na poloze spuštěnou vstupem do nákupního centra nebo rodičovské kontroly, které upozorní, když dítě opustí bezpečnou zónu. Provádění těchto úloh pomocí nepřetržitých požadavků v reálném čase by bylo velmi neefektivní, spotřebovávalo by nadměrné množství signalizačních prostředků sítě, kapacity zpracování jádra sítě a životnosti baterie UE. LDR to řeší tím, že umožňuje jediným požadavkem definovat plán budoucích akcí. Tím se snižuje signalizační režie, optimalizuje využití síťových prostředků a je šetrnější k omezením napájení UE. Umožnil novou třídu služeb založených na poloze, které jsou proaktivní, plánované nebo spouštěné událostmi, a vytvořil tak základní schopnost pro případy použití Internetu věcí (IoT) a komunikace mezi stroji (M2M) pro sledování, které se objevily později. Jeho zavedení v časovém rámci R99 umožnilo sítím GSM a UMTS nabízet sofistikované přidané služby.

## Klíčové vlastnosti

- Podporuje odložené spouštění na základě absolutního času, periodických intervalů nebo událostí změny oblasti
- Ukládá a spravuje požadavky na určení polohy uvnitř sítě (např. v GMLC) až do aktivace
- Integruje se se všemi standardizovanými metodami určování polohy LCS (síťové, založené na UE, asistované)
- Snižuje zatížení sítě signalizací ve srovnání s opakovanými okamžitými požadavky na polohu
- Umožňuje periodické nebo událostmi řízené sledování šetrné k baterii pro UE
- Zahrnuje mechanismy pro zrušení požadavku, jeho úpravu a kontrolu autorizace z hlediska ochrany soukromí

## Související pojmy

- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.731** (Rel-16) — 5G LCS Architecture Enhancement Study
- **TS 24.080** (Rel-19) — Mobile radio interface layer 3 supplementary services
- **TS 24.571** (Rel-19) — Control Plane LCS Procedures
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TS 29.515** (Rel-19) — Ngmlc Service Based Interface Protocol
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 29.572** (Rel-19) — Nlmf Service Based Interface Stage 3

---

📖 **Anglický originál a plná specifikace:** [LDR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ldr/)
