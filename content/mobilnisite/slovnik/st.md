---
slug: "st"
url: "/mobilnisite/slovnik/st/"
type: "slovnik"
title: "ST – Sending Terminated"
date: 2025-01-01
abbr: "ST"
fullName: "Sending Terminated"
category: "Services"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/st/"
summary: "Služební schopnost pro ukončení odesílání mediálních toků, jako je video nebo audio, v multimediálních relacích. Používá se v IMS (IP Multimedia Subsystem) ke správě kontinuity relace a řízení prostře"
---

ST je služební schopnost pro ukončení odesílání mediálních toků v IMS multimediálních relacích za účelem správy kontinuity relace a řízení prostředků.

## Popis

Sending Terminated (ST) je služební schopnost definovaná v rámci architektury IP Multimedia Subsystem (IMS) 3GPP, konkrétně související s řízením relací a manipulací s médii. Funguje jako součást širších mechanismů Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) a Session Description Protocol ([SDP](/mobilnisite/slovnik/sdp/)), které se používají k navázání, úpravě a ukončení multimediálních relací. ST se vyvolá, když uživatel nebo síťový prvek rozhodne zastavit odesílání médií v jednom směru v probíhající relaci, což může být způsobeno akcí uživatele (např. ztlumení hovoru), síťovými podmínkami nebo servisní logikou. Tato schopnost je klíčová pro nezávislé řízení obousměrných mediálních toků a umožňuje scénáře jako hold/resume nebo asymetrické mediální relace, kdy vysílá pouze jedna strana.

Z architektonického hlediska je ST implementována v základních prvcích IMS, jako je Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) a Application Servers ([AS](/mobilnisite/slovnik/as/)), které zpracovávají signalizaci SIP. Při aktivaci ST síť odešle specifické zprávy SIP (např. re-INVITE nebo UPDATE) s atributy SDP, které indikují ukončení odesílání médií v daném směru. To zahrnuje aktualizaci parametrů relace, aby odrážely změnu, a zajištění, že přijímající strana je informována a prostředky jako přenašeče v Packet Data Network ([PDN](/mobilnisite/slovnik/pdn/)) jsou odpovídajícím způsobem upraveny. Proces se integruje s frameworky Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) k vynucení QoS a tarifních politik na základě upraveného mediálního toku.

V praxi ST umožňuje funkce jako call hold, kdy uživatel zastaví odesílání audia, ale může jej dále přijímat, nebo úpravy video streamování v reakci na omezení šířky pásma. Spolupracuje s dalšími IMS službami, jako jsou Supplementary Services a Multimedia Telephony (MMTel), a poskytuje detailní kontrolu nad mediálními toky. Mezi klíčové komponenty patří základní síť IMS, UE (User Equipment) podporující SIP a rozhraní jako Gm (mezi UE a IMS) a [ISC](/mobilnisite/slovnik/isc/) (mezi [CSCF](/mobilnisite/slovnik/cscf/) a AS). Úlohou ST je zachovat integritu relace při optimalizaci síťových prostředků, zabránit zbytečnému přenosu dat a sladit se s uživatelskými preferencemi nebo síťovými politikami.

## K čemu slouží

ST bylo zavedeno, aby řešilo potřebu detailní kontroly nad mediálními toky v IP multimediálních službách, zejména v rámci IMS. Před jeho standardizací správa relací často postrádala mechanismy pro nezávislé ukončení odesílání v jednom směru bez ukončení celé relace, což vedlo k neefektivitám. Například v raných VoIP systémech mohlo převedení hovoru do režimu hold vyžadovat ukončení a opětovné navázání relace, což způsobovalo zpoždění a možné narušení služby. ST to řeší tím, že umožňuje asymetrické zacházení s médii, což sítím umožňuje šetřit prostředky a zlepšovat uživatelský komfort.

Historicky, jak se 3GPP vyvíjelo od okruhově přepínaných k paketově přepínaným sítím ve verzi Release 8, se IMS stalo ústředním pro poskytování pokročilých komunikačních služeb. ST vzniklo jako součást tohoto posunu na podporu pokročilých funkcí, jako je multimediální konferencing a videohovory, kde jsou dynamické úpravy médií běžné. Řeší omezení dřívějších protokolů, které zacházely s mediálními toky jako se vším nebo ničím, tím, že poskytuje standardizovaný způsob pro úpravy relací v reálném čase. To je motivováno rostoucí poptávkou po flexibilních a efektivních službách, které se přizpůsobují uživatelským akcím a síťovým podmínkám, jako například v nasazeních LTE a 5G.

Navíc ST usnadňuje servisní inovace tím, že operátorům umožňuje nabízet vylepšené schopnosti, jako je selektivní přenos médií, což je klíčové pro aplikace jako vzdálený dohled nebo interaktivní hry. Integruje se se systémy QoS a účtování, což zajišťuje vynucení síťových politik při změnách mediálních toků. Řešením těchto problémů ST přispívá k celkovému cíli IMS: poskytovat spolehlivé, škálovatelné multimediální služby napříč různými přístupovými technologiemi.

## Klíčové vlastnosti

- Umožňuje ukončení odesílání médií v jednom směru v rámci relace
- Integruje se s protokoly SIP a SDP pro signalizaci a popis relace
- Podporuje asymetrické mediální toky pro funkce jako call hold
- Spolupracuje se základními prvky IMS (např. S-CSCF, AS) pro servisní logiku
- Soulad s Policy and Charging Control (PCC) pro správu prostředků
- Umožňuje dynamické úpravy relací bez úplného ukončení

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [SDP – Service Discovery Protocol](/mobilnisite/slovnik/sdp/)
- [MMTEL – Multimedia Telephony Service for IMS](/mobilnisite/slovnik/mmtel/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)

## Definující specifikace

- **TS 24.216** (Rel-19) — Communication Continuity Management Object
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 33.805** (Rel-12) — 3GPP Network Product Security Assurance Methodology
- **TR 38.901** (Rel-19) — Channel Model for 0.5-100 GHz

---

📖 **Anglický originál a plná specifikace:** [ST na 3GPP Explorer](https://3gpp-explorer.com/glossary/st/)
