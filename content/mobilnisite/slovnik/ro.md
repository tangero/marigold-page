---
slug: "ro"
url: "/mobilnisite/slovnik/ro/"
type: "slovnik"
title: "RO – Registration Operator"
date: 2026-01-01
abbr: "RO"
fullName: "Registration Operator"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ro/"
summary: "Síťový operátor zodpovědný za registraci a správu předplatného a služebního profilu uživatelského zařízení (UE) v rámci sítě 5G, zejména ve scénářích zahrnujících sekundární autentizaci nebo síťové ře"
---

RO (Registration Operator) je síťový operátor zodpovědný za registraci a správu předplatného a služebního profilu uživatelského zařízení (UE) pro konkrétní službu nebo síťový řez v rámci sítě 5G.

## Popis

Registration Operator (RO) je funkční role definovaná v architektuře systému 5G (5GS), specifikovaná v kontextech jako je sekundární autentizace/autorizace a síťově-řezově specifická autentizace a autorizace ([NSSAA](/mobilnisite/slovnik/nssaa/)). Koncepčně je RO síťový operátor – odlišný od, ale případně totožný s, primární obsluhující [PLMN](/mobilnisite/slovnik/plmn/) (Public Land Mobile Network) – který drží předplatné a služební profil uživatele pro konkrétní službu nebo instanci síťového řezu. Když UE požaduje přístup ke službě vyžadující samostatné přihlašovací údaje (např. podniková služba, služba aplikace třetí strany nebo specifický síťový řez), může primární síť (navštívená PLMN nebo domácí PLMN) komunikovat s RO, aby uživatele autentizovala specificky pro tento kontext služby.

Architektonicky RO komunikuje s funkcemi 5G jádra, především s Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) a Network Slice-Specific Authentication and Authorization Function ([NSSAAF](/mobilnisite/slovnik/nssaaf/)). V toku sekundární autentizace UE naváže primární spojení se svou domácí PLMN ([HPLMN](/mobilnisite/slovnik/hplmn/)). Při pokusu o přístup ke službě vyžadující sekundární autentizaci může Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) spustit autentizační dialog založený na [EAP](/mobilnisite/slovnik/eap/). AUSF v HPLMN pak vystupuje jako EAP autentizátor, proxyuje autentizační zprávy k autentizačnímu serveru RO, který drží uživatelovy přihlašovací údaje pro danou službu. RO ověří přihlašovací údaje a autorizuje přístup k požadované službě nebo řezu.

V proceduře NSSAA pro síťové řezy, když UE požaduje řez vyžadující samostatnou autentizaci ([S-NSSAI](/mobilnisite/slovnik/s-nssai/) s nastavenou povinnou autentizací/autorizací), AMF vyvolá NSSAAF. NSSAAF komunikuje s RO asociovaným s tímto konkrétním S-NSSAI. RO provede řezově specifickou autentizaci a autorizaci a vrátí výsledek NSSAAF a AMF, které pak povolí nebo zamítnou registraci UE pro tento řez. Role RO tedy decentralizuje autentizační autoritu, umožňuje víceoperátorské poskytování služeb, integraci podnikových sítí a flexibilní obchodní modely, kde je poskytovatel služby (RO) oddělen od poskytovatele konektivity (PLMN).

## K čemu slouží

Koncept Registration Operator byl zaveden, aby řešil vyvíjející se obchodní a technickou krajinu 5G, zejména síťové řezy a architekturu orientovanou na služby. Předchozí generace (4G a starší) se primárně spoléhaly na jedinou, monolitickou autentizaci prostřednictvím domácí PLMN s využitím přihlašovacích údajů z (U)SIM. Tento model byl nedostatečný pro vizi 5G podporující rozmanité vertikální odvětví (např. automobilový průmysl, zdravotnictví, výroba), kde poskytovatel služby třetí strany (jako podnik nebo cloudový poskytovatel) potřebuje nezávisle na mobilním operátorovi poskytujícím rádiovou konektivitu kontrolovat přístup ke svému specifickému síťovému řezu nebo službě.

Jeho zavedení řeší problém delegované autentizace a autorizace. Bez modelu RO by HPLMN musela spravovat všechny přihlašovací údaje pro všechny možné služby třetích stran, což by vytvářelo problémy se škálovatelností, bezpečností a složitostí obchodních vztahů. RO umožňuje poskytovateli služby zachovat si vlastnictví nad služební identitou a politikami uživatele. To umožňuje nové obchodní modely, například když vlastník továrny (RO) uzavře smlouvu s mobilním operátorem na privátní 5G řez a přímo spravuje, kteří zaměstnanci nebo zařízení k tomuto řezu mohou přistupovat.

Dále RO usnadňuje regulatorní a provozní oddělení. Ve scénářích jako jsou neutrální hostitelské sítě nebo víceoperátorová jádra sítí (MOCN) mohou různí operátoři vystupovat jako RO pro své příslušné účastníky sdílející stejnou rádiovou infrastrukturu. Také zvyšuje bezpečnost kompartmentalizací autentizačních domén; prolomení přihlašovacích údajů u RO třetí strany neohrozí uživatelovo primární předplatné mobilní sítě. Motivace vychází z práce 3GPP na sekundární autentizaci (z EPC) a její formalizaci v 5G pro řezově specifickou kontrolu přístupu, čímž poskytuje architektonické háčky potřebné pro skutečně multi-tenantní, na služby orientovaný ekosystém 5G.

## Klíčové vlastnosti

- Funkční role pro správu předplatného specifického pro službu nebo řez
- Provádí sekundární autentizaci/autorizaci oddělenou od primární 3GPP autentizace
- Komunikuje s 5GC NFs jako AUSF a NSSAAF přes standardní rozhraní
- Umožňuje víceoperátorské modely poskytování služeb a modely třetích stran
- Klíčová pro Network Slice-Specific Authentication and Authorization (NSSAA)
- Umožňuje poskytovatelům služeb zachovat si kontrolu nad politikami přístupu uživatelů

## Související pojmy

- [NSSAA – Network Slice-Specific Authentication and Authorization](/mobilnisite/slovnik/nssaa/)
- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [S-NSSAI – Single Network Slice Selection Assistance Information](/mobilnisite/slovnik/s-nssai/)

## Definující specifikace

- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TS 32.522** (Rel-11) — SON Policy NRM IRP Information Service
- **TS 33.812** (Rel-9) — M2M Remote Subscription Management Security
- **TR 38.864** (Rel-18) — Technical Report on Network Energy Savings for NR

---

📖 **Anglický originál a plná specifikace:** [RO na 3GPP Explorer](https://3gpp-explorer.com/glossary/ro/)
