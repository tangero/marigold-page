---
slug: "n-os"
url: "/mobilnisite/slovnik/n-os/"
type: "slovnik"
title: "N-OS – Network Management Layer-Operations Systems"
date: 2025-01-01
abbr: "N-OS"
fullName: "Network Management Layer-Operations Systems"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/n-os/"
summary: "Network Management Layer-Operations Systems (N-OS) jsou vysokourovňové systémy provozní podpory (OSS), které spravují celou telekomunikační síť. Poskytují FCAPS (Fault, Configuration, Accounting, Perf"
---

N-OS je vysokourovňový systém provozní podpory (OSS), který spravuje celou telekomunikační síť a poskytuje FCAPS funkce řízení pro sledování, řízení a fakturaci síťových služeb.

## Popis

Network Management Layer-Operations Systems (N-OS) představují vrchní vrstvu v hierarchii Telecommunications Management Network (TMN) dle 3GPP, konkrétně Network Management Layer ([NML](/mobilnisite/slovnik/nml/)). N-OS jsou komplexní systémy provozní podpory, které poskytují celosíťový, často technologií nezávislý pohled a řízení spravované sítě. Agregují a korelují informace ze systémů podřízené Element Management Layer ([EML](/mobilnisite/slovnik/eml/)), které spravují konkrétní síťové prvky nebo domény (např. RAN nebo Core). N-OS implementují základní FCAPS (Fault, Configuration, Accounting, Performance, and Security) funkcionalitu řízení v celosíťovém měřítku.

Z architektonického hlediska N-OS komunikuje s více Element Management Systems ([EMS](/mobilnisite/slovnik/ems/)) prostřednictvím standardizovaných rozhraní (často založených na [CORBA](/mobilnisite/slovnik/corba/), SNMP nebo později na webových službách podle specifikací 3GPP jako 32.102 a 32.819). Zpracovává a ukládá velké objemy dat o výkonu, informací o alarmech a konfiguračních modelů za účelem podpory zajištění služeb, plánování kapacity a analýzy kořenových příčin. Mezi klíčové komponenty patří centralizovaná databáze, rozhraní směrem k Business Support Systems ([BSS](/mobilnisite/slovnik/bss/)) a pokročilé analytické a reportovací nástroje.

Princip činnosti zahrnuje sběr dat z EMS, normalizaci těchto dat do společného informačního modelu a následnou analýzu. Například N-OS může korelovat nárůst alarmů o ztrátě hovorů z určité geografické oblasti s nedávnými změnami konfigurace a metrikami výkonu, aby identifikoval kořenovou příčinu. Také zvládá správu na úrovni služeb, kdy převádí obchodní definice služeb (např. QoS úrovně „gold“) na celosíťové konfigurační politiky, které jsou distribuovány k příslušným EMS a síťovým prvkům. Jeho úlohou je umožnit efektivní, automatizovaný a inteligentní provoz rozsáhlých sítí s více dodavateli a technologiemi.

## K čemu slouží

N-OS existuje, aby řešil problém řízení stále složitějších telekomunikačních sítí s více dodavateli a technologiemi z holistické, na služby orientované perspektivy. Jak se sítě vyvinuly z jednoduchých hlasových systémů na komplexní platformy pro datové a multimediální služby, správa jednotlivých prvků izolovaně se stala neefektivní a náchylnou k chybám. N-OS poskytuje jednotnou vrstvu řízení, která abstrahuje složitost podkladové sítě a umožňuje operátorům spravovat služby, kvalitu a uživatelský zážitek, nikoliv pouze jednotlivá zařízení.

Historická motivace vychází z rámce TMN, který byl vyvinut pro zavedení řádu a standardizace do řízení sítí. Před existencí těchto vrstvených architektur se operátoři spoléhali na proprietární manažery prvků s omezenou integrací, což činilo globální úkoly jako poskytování služeb, korelaci chyb a sledování výkonu od konce ke konci nesmírně obtížnými a manuálními. N-OS řeší tato omezení tím, že poskytuje standardizovaný, agregovaný pohled a bod řízení. Jeho vznik byl motivován potřebou provozní efektivity, zkrácení doby uvedení nových služeb na trh a schopností garantovat smlouvy o úrovni služeb (SLA) napříč heterogenním síťovým prostředím.

## Klíčové vlastnosti

- Celosíťové (end-to-end) FCAPS řízení napříč síťovými doménami
- Agregace a korelace dat z více Element Management Systems (EMS)
- Správa na úrovni služeb a sledování SLA
- Rozhraní pro integraci s Business Support Systems (BSS)
- Podpora síťových prostředí s více dodavateli a technologiemi
- Pokročilá analýza pro určení kořenové příčiny a plánování kapacity

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.819** (Rel-8) — Element Management Layer OS Functions

---

📖 **Anglický originál a plná specifikace:** [N-OS na 3GPP Explorer](https://3gpp-explorer.com/glossary/n-os/)
