---
slug: "msh"
url: "/mobilnisite/slovnik/msh/"
type: "slovnik"
title: "MSH – Media Session Handler"
date: 2025-01-01
abbr: "MSH"
fullName: "Media Session Handler"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/msh/"
summary: "Media Session Handler (MSH) je funkční entita v architektuře 5G Media Streaming. Spravuje zřizování, řízení a ukončování relací pro doručování médií pro streamovací služby, jako je adaptivní streamová"
---

MSH je funkční entita v architektuře 5G Media Streaming, která spravuje zřizování, řízení a ukončování relací pro doručování médií a funguje jako zprostředkovatel mezi aplikačním klientem a sítí pro doručování médií.

## Popis

Media Session Handler (MSH) je funkce založená v jádru sítě, specifikovaná v rámci frameworku 5G Media Streaming ([5GMS](/mobilnisite/slovnik/5gms/)) (3GPP TS 26.501 a související dokumenty). Nachází se v aplikační vrstvě, typicky v doméně poskytovatele aplikace 5GMS nebo jako důvěryhodná aplikační funkce rozhraní s 5G Core. Primární role MSH je fungovat jako řadič relace pro doručování médií. Nedoručuje samotný mediální obsah, ale orchestruje relaci interakcí s funkcí řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) v 5G Core Network a s klientem pro mediální streamování ([MSC](/mobilnisite/slovnik/msc/)) v uživatelském zařízení (UE).

Architektonicky MSH spolupracuje s funkcí pro distribuci médií ([MDF](/mobilnisite/slovnik/mdf/)), která zajišťuje skutečné ukládání do mezipaměti a doručování obsahu. Když klient pro mediální streamování (MSC) zahájí požadavek na streamovací službu, kontaktuje MSH. MSH ověří klienta a požadavek, určí příslušné zásady pro doručování médií (např. požadovaný datový tok, úrovně QoS) a tyto požadavky vyjedná s 5G Core přes rozhraní N5 s PCF. To vede k zřízení vyhrazeného QoS toku pro mediální relaci, což zajišťuje přidělení síťových prostředků podle potřeb streamovací služby. MSH následně poskytne klientovi potřebný popis relace, typicky Media Presentation Description ([MPD](/mobilnisite/slovnik/mpd/)) pro streamování založené na [DASH](/mobilnisite/slovnik/dash/), který obsahuje URL adresy pro mediální segmenty hostované MDF.

Během aktivní relace MSH sleduje stav relace a může dynamicky ovlivňovat doručování na základě síťových podmínek nebo požadavků aplikace. Například, pokud síť detekuje přetížení, může PCF informovat MSH, která pak může instruovat klienta (prostřednictvím MPD), aby přešel na reprezentaci s nižším datovým tokem. Naopak, pokud je k dispozici vysoká šířka pásma, může MSH umožnit klientovi přejít na proud vyšší kvality. Také zpracovává události relace, jako je pozastavení, obnovení a ukončení, a zajišťuje řádnou koordinaci s 5G Core pro aktivaci nebo uvolnění odpovídajících QoS prostředků. MSH tedy abstrahuje složitost řízení síťových politik 5G od mediálního klienta a umožňuje tak efektivní, QoS-aware a adaptivní služby mediálního streamování.

## K čemu slouží

Media Session Handler byl představen v 5G Release 17 jako součást podpůrných prostředků pro 5G Media Streaming, aby řešil omezení streamování typu over-the-top ([OTT](/mobilnisite/slovnik/ott/)) v mobilních prostředích. Před [5GMS](/mobilnisite/slovnik/5gms/) streamovací klienti fungovali nezávisle na podkladové síti a vyžadovali obsah od CDN bez jakékoli koordinace se sítí mobilního operátora. To vedlo k neefektivitám, jako je suboptimální výběr datového toku během přetížení, neschopnost garantovat kvalitu a absence síťově asistovaných optimalizací. MSH byl vytvořen, aby tuto mezeru překlenul, a poskytuje standardizované rozhraní pro streamovací aplikace, aby mohly využívat možnosti sítě 5G.

Klíčový problém, který řeší, je nedostatek integrace mezi streamováním na aplikační vrstvě a QoS a řízením politik na síťové vrstvě. Fungováním jako centralizovaný řadič relace umožňuje MSH poskytovateli služeb vyžádat si konkrétní síťové prostředky (jako je tok s garantovaným datovým tokem) pro prémiovou streamovací relaci. To umožňuje skutečně diferencované služby, jako je garantované ultra-high-definition video nebo streamování s nízkou latencí, které bylo obtížné zajistit s best-effort přístupem k internetu. Jeho vytvoření bylo motivováno požadavkem průmyslu na služby streamování na úrovni operátora, síťové segmenty pro média a potřebou efektivnějšího využití prostředků sítě 5G pro aplikace s vysokou šířkou pásma.

## Klíčové vlastnosti

- Orchestruje zřizování, změnu a ukončení relací pro 5G mediální streamování
- Komunikuje s funkcí řízení politik (PCF) v 5G Core přes rozhraní N5 pro dynamickou autorizaci QoS
- Poskytuje klientovi pro mediální streamování (MSC) informace pro popis relace (např. DASH MPD)
- Umožňuje síťově asistované dynamické adaptivní streamování na základě aktuálních síťových podmínek
- Podporuje integraci s funkcí pro distribuci médií (MDF) pro řízení doručování obsahu
- Usnadňuje přidělování síťových prostředků a vynucování politik s ohledem na aplikaci

## Definující specifikace

- **TS 26.506** (Rel-19) — Real-Time Media Communication Architecture for 5G
- **TS 26.565** (Rel-19) — Split Rendering Media Service Enabler
- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- **TS 26.847** (Rel-19) — AI/ML Evaluation in 5G Media Services
- **TR 26.857** (Rel-18) — Technical Report on Media Service Enablers
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [MSH na 3GPP Explorer](https://3gpp-explorer.com/glossary/msh/)
