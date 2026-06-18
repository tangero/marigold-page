---
slug: "dcca"
url: "/mobilnisite/slovnik/dcca/"
type: "slovnik"
title: "DCCA – Diameter Credit Control Application"
date: 2025-01-01
abbr: "DCCA"
fullName: "Diameter Credit Control Application"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dcca/"
summary: "DCCA je protokol založený na Diameteru pro řízení kreditu v reálném čase v sítích 3GPP. Umožňuje poskytovatelům služeb spravovat předplacené i postpaid účtování, vynucovat výdajové limity a řídit využ"
---

DCCA je protokol založený na Diameteru pro řízení kreditu v reálném čase v sítích 3GPP, který umožňuje poskytovatelům služeb spravovat účtování, vynucovat výdajové limity a řídit využívání služeb.

## Popis

Aplikace Diameter Credit Control (DCCA) je standardizovaný protokol v rámci architektury 3GPP, který poskytuje rámec pro autorizaci kreditu a správu kvót v reálném čase. Funguje jako aplikace nad základním protokolem Diameter ([RFC](/mobilnisite/slovnik/rfc/) 6733) a využívá jeho spolehlivý transport, mechanismy převzetí služeb při selhání (failover) a bezpečnostní funkce. DCCA definuje specifické kódy příkazů, páry atribut-hodnota ([AVP](/mobilnisite/slovnik/avp/)) a stavové automaty pro usnadnění komunikace mezi síťovými elementy poskytujícími služby (klienti Diameteru) a centrálním serverem řízení kreditu (server Diameteru). Tato komunikace je klíčová pro implementaci systémů online účtování ([OCS](/mobilnisite/slovnik/ocs/)), kde musí být autorizace služby udělena v reálném čase na základě stavu účtu uživatele nebo jeho kreditního limitu.

Základní operace DCCA se točí kolem modelu žádost-a-povolení pro servisní jednotky. Když uživatel zahájí službu (např. datovou relaci, hovor nebo [SMS](/mobilnisite/slovnik/sms/)), síťový element (např. [P-GW](/mobilnisite/slovnik/p-gw/), [S-CSCF](/mobilnisite/slovnik/s-cscf/)) fungující jako klient řízení kreditu Diameter (CC-Client) odešle zprávu Credit-Control-Request ([CCR](/mobilnisite/slovnik/ccr/)) na server řízení kreditu (CC-Server, typicky součást OCS). Tato žádost obsahuje informace jako identita uživatele (např. [IMSI](/mobilnisite/slovnik/imsi/), MSISDN), požadovaná služba a požadované servisní jednotky. CC-Server vyhodnotí účet uživatele, aplikuje tarifikaci a rozhodne, zda je kredit k dispozici. Následně odpoví zprávou Credit-Control-Answer (CCA), která buď udělí kvótu servisních jednotek (např. objem dat, časové trvání), nebo žádost zamítne. Klient pak sleduje spotřebu uživatele vůči této udělené kvótě.

Jak uživatel službu spotřebovává, CC-Client sleduje využití. Když je udělená kvóta vyčerpána nebo dosažen určitý práh, klient odešle průběžnou CCR (UPDATE) s žádostí o další jednotky. Po ukončení služby je odeslána finální CCR (TERMINATION), která nahlásí celkové spotřebované jednotky, což serveru umožní přesně odečíst částku z účtu uživatele. Tato stavová, relací založená interakce zajišťuje přesné účtování v reálném čase. DCCA podporuje současně více servisních kontextů pro jednoho uživatele prostřednictvím různých ratingových skupin a identifikátorů služeb, což umožňuje komplexní tarifní plány (např. oddělené kvóty pro hlas, data a prémiový obsah).

Mezi klíčové architektonické komponenty patří CC-Client, vestavěný do síťových funkcí jako PCEF (Policy and Charging Enforcement Function) pro data nebo S-CSCF pro IMS služby, a CC-Server uvnitř OCS. Protokol definuje několik AVP specifických pro řízení kreditu, jako jsou CC-Request-Type, CC-Request-Number, Granted-Service-Unit, Used-Service-Unit, Validity-Time a Multiple-Services-Credit-Control pro správu více kvót. Role DCCA je nedílnou součástí architektury 3GPP Online Charging System (OCS), neboť poskytuje standardizované signalizační rozhraní (referenční bod Gy) mezi PCEF a OCS a referenční bod Ro pro online účtování v IMS.

## K čemu slouží

DCCA byla vytvořena, aby řešila kritickou potřebu standardizovaného, robustního a v reálném čase fungujícího mechanismu řízení kreditu v rozvíjejících se telekomunikačních sítích, zejména s nástupem paketově přepínaných služeb a předplacených obchodních modelů. Před její standardizací se pro podobné účely používaly proprietární protokoly nebo adaptace protokolu RADIUS. Tato řešení byla často omezená škálovatelností, postrádala podporu pro komplexní relací založené služby a ztěžovala interoperabilitu mezi síťovými elementy a fakturačními systémy různých výrobců. Přechod na plně IP sítě a zavádění bohatých, relací založených služeb ve 3G a později 4G/LTE si vyžádaly sofistikovanější přístup.

Primární problém, který DCCA řeší, je zajištění výnosů pro poskytovatele služeb nabízejících předplacené a konvergentní účtování. Zabraňuje úniku výnosů tím, že zajišťuje poskytnutí služeb až po potvrzení, že uživatel má dostatečný kredit nebo kvótu. Umožňuje řízení v reálném čase, což operátorům dává možnost nabízet modely 'pay-as-you-go' pro data, hlas a zprávy, které jsou dominantní na mnoha globálních trzích. Dále DCCA podporuje pokročilé obchodní modely, jako je kontrola výdajových limitů pro postpaid uživatele, služební plány založené na kvótách (např. denní datové balíčky) a notifikace o stavu účtu v reálném čase. Její vytvoření bylo motivováno omezeními starších mechanismů založených na RADIUS, které byly bezstavové, měly omezený prostor pro atributy a postrádaly inherentní spolehlivost a bezpečnostní funkce Diameteru. DCCA, postavená na Diameteru, poskytla stavový, relacemi orientovaný, rozšiřitelný a bezpečnější protokol navržený pro komplexní účtovací scénáře moderních mobilních sítí.

## Klíčové vlastnosti

- Autorizace kreditu a správa kvót v reálném čase
- Stavový, relací založený protokol pro přesné sledování využití
- Podpora více souběžných služeb na uživatele prostřednictvím AVP Multiple-Services-Credit-Control
- Přímá integrace s architekturou 3GPP Online Charging System (OCS)
- Definuje standardizované referenční body Gy (PCEF-OCS) a Ro (IMS-OCS)
- Mechanismy převzetí služeb při selhání a návratu (failover/failback) převzaté ze základního protokolu Diameter

## Definující specifikace

- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.270** (Rel-19) — MMS Charging Management Specification
- **TS 32.271** (Rel-19) — 3GPP LCS Charging Management Spec
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.276** (Rel-19) — VCS Online Charging from Proxy Function
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification
- **TS 32.281** (Rel-19) — Announcement Service for Online Charging
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- **TS 32.869** (Rel-15) — Diameter Overload Control for Charging Interfaces
- **TS 32.870** (Rel-15) — Study on 3GPP Charging Forward Compatibility

---

📖 **Anglický originál a plná specifikace:** [DCCA na 3GPP Explorer](https://3gpp-explorer.com/glossary/dcca/)
