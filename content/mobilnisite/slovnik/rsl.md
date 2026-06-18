---
slug: "rsl"
url: "/mobilnisite/slovnik/rsl/"
type: "slovnik"
title: "RSL – Radio Signalling Link"
date: 2025-01-01
abbr: "RSL"
fullName: "Radio Signalling Link"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rsl/"
summary: "Logický komunikační kanál vyhrazený pro přenos signalizace řídicí roviny mezi síťovými entitami v rádiové přístupové vrstvě. Přepravuje klíčové zprávy pro správu mobility, řízení rádiových zdrojů a na"
---

RSL je logický kanál vyhrazený pro přenos signalizace řídicí roviny mezi síťovými entitami v rádiové přístupové vrstvě pro správu mobility, řízení rádiových zdrojů a navázání spojení.

## Popis

Radio Signalling Link (RSL) je základní logický kanál v mobilních sítích 3GPP, který je odpovědný za přenos signalizačních zpráv řídicí roviny přes rádiové rozhraní. Funguje v rámci vrstvy rádiové přístupové sítě (RAN), konkrétně mezi uživatelským zařízením (UE) a síťovým rádiovým řadičem (např. Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) v UMTS/[UTRAN](/mobilnisite/slovnik/utran/) nebo základnovou stanicí (eNodeB/gNB) v LTE/5G NR). RSL není fyzický vodič, ale logická cesta zřízená přes sdílené rádiové médium, kterou pečlivě spravují nižší vrstvy (fyzická vrstva a vrstva datového spoje) za účelem zajištění spolehlivosti.

Architektonicky je RSL implementován pomocí vyhrazených signalizačních rádiových přenosových kanálů ([SRB](/mobilnisite/slovnik/srb/)). V protokolovém zásobníku jsou signalizační zprávy z vrstvy řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) zapouzdřeny a přenášeny právě přes tyto SRB. Fyzická vrstva poskytuje skutečné přenosové zdroje (časové sloty, kmitočtové nosné, rozprostírací kódy), zatímco vrstva řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) zajišťuje plánování a stanovení priority logických kanálů, což garantuje, že kritická signalizace RSL získá přístup k rádiovým zdrojům i při přetížení. Vrstva řízení rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)) pro RSL typicky pracuje v potvrzovaném režimu ([AM](/mobilnisite/slovnik/am/)), poskytuje retransmise a zaručuje tak bezchybné doručení signalizačních zpráv, což je klíčové pro stabilitu sítě.

RSL přenáší širokou škálu nezbytných řídicích zpráv. Patří mezi ně vysílání systémových informací, které informují UE o konfiguraci sítě, procedury navázání a uvolnění RRC spojení, příkazy pro aktivaci zabezpečení (šifrování a ochrana integrity), povely k předání spojení, konfigurace hlášení měření a oznámení o volání. Výkon a spolehlivost RSL přímo ovlivňují klíčové uživatelské zkušenosti: dobu navazování hovorů, úspěšnost předání spojení a schopnost sítě efektivně spravovat své rádiové zdroje. Jakékoli selhání nebo výrazné zpoždění na RSL může vést k přerušeným spojením, neúspěšným předáním spojení nebo neschopnosti UE přistoupit k síti.

## K čemu slouží

Radio Signalling Link byl definován za účelem vytvoření jasného oddělení přenosů řídicí a uživatelské roviny přes inherentně nespolehlivé a sdílené rádiové médium. V raných mobilních systémech bylo zajištění spolehlivého doručení kritických síťových řídicích příkazů identifikováno jako odlišná výzva od doručování uživatelských dat. Uživatelská data (uživatelská rovina) mohla tolerovat určité zpoždění a dokonce i ztrátu paketů (např. díky retransmiscím na vyšších vrstvách v TCP), avšak signalizační zprávy pro správu mobility a relací vyžadují deterministické, nízkolatenční a vysoce spolehlivé doručení. Koncept RSL formalizuje vyhrazené mechanismy pro splnění těchto přísných požadavků.

Řeší problém, jak spravovat síť, když je základní komunikační kanál vysílací, sdílený a náchylný k chybám. Bez vyhrazeného, spolehlivě spravovaného signalizačního spoje by mohly být řídicí zprávy ztraceny kvůli rušení nebo kolizi, což by ponechalo UE v neznámém stavu a síť by nebyla schopna efektivně koordinovat zdroje. RSL poskytuje pro tento dialog prioritizovaný a chráněný kanál. Jeho vytvoření bylo motivováno potřebou robustní správy mobility, jak se sítě vyvíjely od jednoduchého pokrytí ke komplexním, vícebuněčným prostředím s předáváním spojení. RSL také podporuje nezbytné síťově řízené procedury, jako je řízení výkonu, řízení přístupu a vyvažování zátěže, které všechny závisí na včasné výměně signalizačních zpráv.

Dále RSL poskytuje základ pro zabezpečení sítě. Signalizační zprávy, které aktivují šifrování a ochranu integrity, jsou samy odesílány přes RSL (před aktivací mohou být odesílány v čistém textu nebo s výchozí ochranou). Bezpečný a spolehlivý RSL je tedy předpokladem pro navázání bezpečného uživatelského spojení. Standardizací konceptu RSL zajistil 3GPP, aby všechny kompatibilní sítě implementovaly konzistentní a robustní metodu pro komunikaci řídicí roviny, což je základním kamenem spolehlivosti, bezpečnosti a efektivity celulárních sítí napříč všemi generacemi od UMTS dále.

## Klíčové vlastnosti

- Vyhrazený logický kanál pro signalizaci řídicí roviny přes rádiové rozhraní
- Implementován pomocí signalizačních rádiových přenosových kanálů (SRB) s plánováním vysoké priority
- Typicky využívá potvrzovaný režim (AM) vrstvy RLC pro garantované, bezchybné doručení
- Přenáší kritické zprávy pro řízení RRC spojení, správu mobility a zabezpečení
- Základní pro spolehlivé vysílání systémových informací a volání
- Poskytuje přenosovou vrstvu pro zprávy protokolu řízení rádiových zdrojů (RRC)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [RSL na 3GPP Explorer](https://3gpp-explorer.com/glossary/rsl/)
