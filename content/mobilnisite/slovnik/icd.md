---
slug: "icd"
url: "/mobilnisite/slovnik/icd/"
type: "slovnik"
title: "ICD – Interface Control Document"
date: 2025-01-01
abbr: "ICD"
fullName: "Interface Control Document"
category: "Interface"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/icd/"
summary: "Specifikační dokument 3GPP, který definuje detailní řídicí procedury, formáty zpráv a informační toky pro konkrétní rozhraní mezi síťovými prvky. Zajišťuje interoperabilitu mezi zařízeními od různých"
---

ICD je specifikační dokument 3GPP, který definuje řídicí procedury, formáty zpráv a informační toky pro konkrétní rozhraní mezi síťovými prvky, aby byla zajištěna interoperabilita.

## Popis

Interface Control Document (ICD) je komplexní technická specifikace v rámci sady standardů 3GPP, která poskytuje definitivní návod pro implementaci konkrétního rozhraní. Detaily popisuje přesné protokolové zásobníky, sekvence zpráv, kódování informačních elementů a procedurální chování vyžadované pro komunikaci mezi dvěma definovanými síťovými entitami, jako například mezi Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) a NodeB v [UTRAN](/mobilnisite/slovnik/utran/) (rozhraní Iub) nebo mezi různými funkcemi core sítě. ICD jde nad rámec obecných architektonických popisů obsažených ve specifikacích fáze 2 (např. TS 23.xxx) tím, že poskytuje implementační detaily fáze 3 (např. TS 25.xxx, 36.xxx, 38.xxx). To zahrnuje ASN.1 definice pro zprávy, přesné stavové automaty pro řídicí procedury a indikátory povinné/volitelné podpory funkcí.

Z architektonického hlediska je ICD svázán s konkrétním fyzickým nebo logickým referenčním bodem (např. Uu, Iub, Iu, [N2](/mobilnisite/slovnik/n2/), N3) v rámci celkové síťové architektury. Definuje komunikaci typu peer-to-peer mezi vrstvami protokolového zásobníku fungujícího na daném rozhraní. Například TS 25.423 je ICD pro rozhraní Iur mezi RNC, které specifikuje protokol Radio Network Subsystem Application Part ([RNSAP](/mobilnisite/slovnik/rnsap/)). Dokument je strukturován tak, aby pokryl všechny aspekty rozhraní: transportní vrstvu sítě (často založenou na IP nebo [ATM](/mobilnisite/slovnik/atm/)), signalizační přenašeče, user plane protokoly pro přenos dat a aplikační signalizační protokoly, které přenášejí vlastní řídicí informace.

Jeho role v síti je zásadní pro multivendorovou interoperabilitu. Dodržováním ICD mohou výrobci zařízení vyvíjet síťové prvky, u kterých je zaručeno, že budou správně komunikovat s prvky od jiných dodavatelů, kteří také dodržují stejný standard. Tím se předchází závislosti na jediném dodavateli, podporuje zdravá konkurence na trhu a umožňuje síťovým operátorům budovat heterogenní sítě. Testy shody, často definované v doprovodných testovacích specifikacích (např. TS 37.571 pro rádiový výkon), jsou založeny na požadavcích stanovených v ICD, což zajišťuje, že implementace jsou nejen syntakticky správné, ale také se za všech specifikovaných podmínek chovají správně.

## K čemu slouží

Primárním účelem Interface Control Document je umožnit a vynutit interoperabilitu v telekomunikačních sítích s více dodavateli. Před standardizovanými rozhraními byli síťoví operátoři často nuceni nakupovat veškeré zařízení pro danou doménu od jediného dodavatele, aby zajistili jeho vzájemnou funkčnost, což vedlo k závislosti na dodavateli, vyšším nákladům a potlačení inovací. Vytvoření detailních ICD jako součásti standardizačního procesu 3GPP tento problém přímo řeší tím, že poskytuje úplný, jednoznačný technický návod, kterého se může držet jakýkoli dodavatel.

Historicky se potřeba takových detailních dokumentů stala kritickou s příchodem 2G GSM a zejména 3G UMTS, kde se síťová architektura stala složitější s jasným oddělením Radio Access Network (RAN) a Core Network (CN) a uvnitř samotného RAN. Motivací bylo rozložit síť na standardizované, nahraditelné stavební bloky. ICD definuje smlouvu mezi těmito bloky. Řeší problém, jak může NodeB od Dodavatele A porozumět a správně reagovat na zprávu Radio Link Setup Request od [RNC](/mobilnisite/slovnik/rnc/) vyrobeného Dodavatelem B.

Dále ICD usnadňují vývoj sítě a zavádění nových funkcí. Když je v releasu 3GPP zavedena nová funkce (jako Carrier Aggregation nebo Dual Connectivity), jsou nezbytná vylepšení dotčených rozhraní pečlivě dokumentována v příslušných ICD. To umožňuje zpětně kompatibilní upgrady a zajišťuje, že nové funkce lze nasadit jednotně v celé síti, dokonce i s vybavením z různých generací nebo od různých dodavatelů. Jsou základem, na kterém jsou budovány stabilní, spolehlivé a rozvíjející se mobilní sítě.

## Klíčové vlastnosti

- Definuje přesné formáty zpráv a kódování informačních elementů (např. pomocí ASN.1)
- Specifikuje detailní procedurální toky a stavové automaty pro signalizaci řízení
- Nastíňuje kompletní protokolový zásobník pro rozhraní, včetně možností transportu
- Udává povinné a volitelné schopnosti pro shodu se standardem
- Poskytuje základ pro testy shody a interoperability
- Zajišťuje jednoznačnou implementaci pro multivendorovou interoperabilitu

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.171** (Rel-19) — 5G A-GNSS UE Positioning Requirements
- **TS 44.031** (Rel-19) — Radio Resource LCS Protocol (RRLP)

---

📖 **Anglický originál a plná specifikace:** [ICD na 3GPP Explorer](https://3gpp-explorer.com/glossary/icd/)
