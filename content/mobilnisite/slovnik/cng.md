---
slug: "cng"
url: "/mobilnisite/slovnik/cng/"
type: "slovnik"
title: "CNG – Comfort Noise Generation"
date: 2025-01-01
abbr: "CNG"
fullName: "Comfort Noise Generation"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cng/"
summary: "Technika používaná v hlasových komunikačních systémech ke generování umělého šumu na pozadí během období ticha v konverzaci. Zabrání vnímání úplného ticha, které může být pro posluchače znepokojivé, a"
---

CNG je technika používaná v hlasových komunikačních systémech ke generování umělého šumu na pozadí během období ticha, aby se zabránilo znepokojivému úplnému tichu a udržel se přirozený zvukový dojem.

## Popis

Comfort Noise Generation (CNG) je funkce zpracování signálu implementovaná v kontextu služeb Voice over IP (VoIP) a telefonie 3GPP, zejména těch používajících kodeky Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)) a Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)). Jejím hlavním úkolem je řídit zvukový dojem během režimů nespojitého přenosu ([DTX](/mobilnisite/slovnik/dtx/)). V DTX vysílač přestane během období ticha (např. když uživatel naslouchá) posílat hlasové rámce za účelem úspory šířky pásma sítě a energie baterie terminálu. Pokud by však přijímač během těchto mezer přehrával absolutní ticho, byl by náhlý kontrast mezi aktivní řečí a naprostým tichem nepřirozený a pro uživatele potenciálně znepokojivý, protože by mohl být zaměněn za přerušení hovoru.

Technicky CNG funguje tak, že vysílací strana (např. User Equipment nebo síťový uzel) analyzuje akustický šum na pozadí přítomný během aktivní řeči. Při vstupu do období ticha periodicky místo běžných řečových rámců vysílá speciální rámce popisovače vložení ticha ([SID](/mobilnisite/slovnik/sid/)). Tyto SID rámce jsou pakety s nízkou přenosovou rychlostí, které obsahují parametry charakterizující spektrální vlastnosti a úroveň energie šumu na pozadí (např. koeficienty lineární prediktivní kódování a zesílení). Dekodér na přijímací straně používá tyto parametry k syntéze odpovídajícího nízkohlučného signálu – komfortního šumu – který je posluchači přehráván během tichých intervalů.

Architektura pro CNG je integrována do činnosti hlasového kodeku a přidružené služby Radio Access Bearer ([RAB](/mobilnisite/slovnik/rab/)) nebo Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)) pro VoIP. Mezi klíčové komponenty patří algoritmus odhadu šumu na straně odesílatele, logika generování SID rámců, plánovač přenosu SID rámců a modul syntézy komfortního šumu na přijímači. Proces je řízen specifickými časovači a prahovými hodnotami definovanými ve specifikacích 3GPP, které určují, kdy po zastavení řeči odeslat první SID rámec, jak často jej aktualizovat a kdy ukončit CNG a vrátit se k plnému přenosu řeči.

Role CNG je klíčová pro Quality of Experience ([QoE](/mobilnisite/slovnik/qoe/)). Zajišťuje kontinuální, přirozeně znějící zvukové pozadí, které maskuje digitální on/off efekt DTX. Toto psychoakustické vyhlazení je základním aspektem metrik vnímané kvality hlasu. Tato technika je používána end-to-end v celém systému 3GPP, od UE přes Radio Access Network (RAN) a Core Network, všude tam, kde jsou zpracovávány hlasové pakety a kde může být DTX aplikováno pro optimalizaci využití zdrojů bez degradace subjektivního poslechového zážitku.

## K čemu slouží

CNG bylo vytvořeno k vyřešení základního problému uživatelského zážitku, který přinesl Discontinuous Transmission ([DTX](/mobilnisite/slovnik/dtx/)) v digitálních celulárních systémech. Rané digitální hlasové kodeky při implementaci DTX pro úsporu energie a šířky pásma vytvářely období absolutního digitálního ticha. Toto 'mrtvé ticho' bylo vnímání rušivé; posluchači nedokázali rozlišit mezi záměrným tichem a selháním hovoru, což vedlo ke zmatení a vnímání špatné kvality hovoru. Úplná absence zvuku také uživatelům ztěžovala posoudit, zda je linka stále spojena, což je často nutilo mluvit hlasitěji nebo opakovaně se ptát 'Haló?'. Toto narušovalo přirozený průběh konverzace.

Motivace pro CNG byla tedy psychoakustická: replikovat konstantní, nízkou úroveň okolního šumu přítomného ve všech reálných akustických prostředích (jako je šum místnosti nebo jemný hluk ulice). Generováním tohoto 'komfortního' šumu systém poskytuje konzistentní zvukové pozadí, které signalizuje aktivní spojení. Historicky byl tento koncept důležitý v analogové telefonii, kde samotný obvod poskytoval slabé syčení, ale byl ztracen v raných čistě digitálních implementacích. CNG tuto přirozenou nápovědu obnovuje digitálně.

Řeší omezení jednoduchého DTX tím, že transformuje techniku šetřící zdroje z potenciálního rizika pro kvalitu na transparentní funkci. Bez CNG by výhody DTX (prodloužená životnost baterie, snížení zahlcení sítě a nižší interference) přicházely za nepřijatelnou cenu uživatelské spokojenosti. CNG je tedy technologií umožňující síťovým operátorům nasazovat efektivní služby VoIP a VoLTE/VoNR bez kompromisů v podobě známého, komfortního zážitku tradičního telefonního hovoru.

## Klíčové vlastnosti

- Generuje umělý šum na pozadí během období ticha v řeči, aby byl udržen přirozený sluchový dojem
- Využívá rámce popisovače vložení ticha (SID) s nízkou přenosovou rychlostí k přenosu parametrů šumu místo plných řečových rámců
- Integrováno s hlasovými kodeky jako AMR a EVS pro plynulý provoz během režimů nespojitého přenosu (DTX)
- Snižuje vnímanou nespojitost a zabraňuje zmatení uživatele, které může vzniknout z absolutního digitálního ticha
- Šetří životnost baterie UE a šířku pásma sítě tím, že umožňuje efektivní provoz DTX bez degradace kvality
- Parametry jsou periodicky aktualizovány, aby sledovaly změny v akustickém prostředí šumu na pozadí

## Související pojmy

- [DTX – Discontinuous Transmission](/mobilnisite/slovnik/dtx/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.523** (Rel-19) — NGCN-NGN Interconnection Scenarios
- **TS 24.525** (Rel-19) — Business Trunking Architecture & Requirements
- **TS 26.094** (Rel-19) — AMR Voice Activity Detector (VAD) Specification
- **TS 26.194** (Rel-19) — Voice Activity Detector for AMR-WB DTX
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.441** (Rel-19) — EVS Audio Processing Introduction
- **TS 26.442** (Rel-19) — EVS Codec Fixed Point ANSI-C Code
- **TS 26.443** (Rel-19) — EVS Codec Floating-Point C Code
- **TS 26.444** (Rel-19) — EVS Codec Conformance Test Sequences
- **TS 26.446** (Rel-19) — EVS Codec AMR-WB Backward Compatibility Spec
- **TS 26.448** (Rel-19) — EVS Jitter Buffer Management Specification
- **TS 26.449** (Rel-19) — EVS Codec Comfort Noise Generation for DTX
- **TS 26.450** (Rel-19) — EVS Codec DTX System Level Aspects
- **TS 26.451** (Rel-19) — EVS Codec Voice Activity Detector (VAD) Specification
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [CNG na 3GPP Explorer](https://3gpp-explorer.com/glossary/cng/)
