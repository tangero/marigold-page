---
slug: "pbx"
url: "/mobilnisite/slovnik/pbx/"
type: "slovnik"
title: "PBX – Private Branch eXchange"
date: 2026-01-01
abbr: "PBX"
fullName: "Private Branch eXchange"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pbx/"
summary: "Privátní telefonní ústředna používaná v rámci podniku pro správu interních hovorů a připojení k veřejné telefonní síti. Poskytuje úsporu nákladů, interní číslování a funkce jako přesměrování hovorů a"
---

PBX je privátní telefonní ústředna používaná v rámci podniku pro správu interních hovorů, připojení k veřejné síti a poskytování funkcí jako přesměrování hovorů, která je integrována pro komunikační služby podniků v 3GPP.

## Popis

Private Branch eXchange (PBX) je privátní telekomunikační síť používaná v rámci organizace. Funguje jako lokální ústředna, která umožňuje uživatelům sdílet určitý počet externích telefonních linek (trunků) pro uskutečňování a přijímání hovorů z veřejné telefonní sítě ([PSTN](/mobilnisite/slovnik/pstn/)) nebo jiných externích sítí. Interně spravuje přípony (extenze), což umožňuje přímé volání mezi uživateli bez použití externích linek. Moderní PBX, často digitální nebo založená na IP, se integruje se sítěmi 3GPP, aby poskytovala podnikové komunikační služby a připojovala mobilní uživatele jako součást firemního telefonního systému.

Architektonicky se PBX skládá z centrální přepínací jednotky, telefonních přístrojů (hardwarové nebo softwarové telefony), trunkových linek k PSTN nebo poskytovateli služeb a interního vedení nebo IP síťových připojení. Zahrnuje software pro zpracování hovorů, směrování a správu funkcí. V kontextu 3GPP se integrace dosahuje pomocí rozhraní jako [PRA](/mobilnisite/slovnik/pra/) (Primary Rate Access) nebo prostřednictvím [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol) trunků připojených k jádrové síti IMS (IP Multimedia Subsystem). To umožňuje, aby byla PBX vnímána jako uzel v širším telekomunikačním ekosystému, podporující služby jako Direct Inward Dialing (DID) a Unified Communications.

Její role v síti 3GPP spočívá v tom, že funguje jako podnikový služební uzel. Umožňuje funkce jako privátní číslovací plány, přesměrování hovorů, konferenční hovory, automatickou sekretářku a hlasovou schránku pro podnikové uživatele, včetně těch, kteří používají mobilní zařízení. PBX se může propojit s jádrovou mobilní sítí (např. přes [MSC](/mobilnisite/slovnik/msc/) pro okruhově přepínané hovory nebo přes IMS pro paketově přepínaný VoIP), což umožňuje bezproblémovou mobilitu a kontinuitu služeb mezi stolními telefony a mobilními přístroji. Tato integrace je klíčová pro strategie Fixed Mobile Convergence ([FMC](/mobilnisite/slovnik/fmc/)).

Klíčové komponenty zahrnují hardwarovou/softwarovou platformu PBX, liniové karty pro analogové/digitální telefony, trunkové karty pro externí připojení a rozhraní pro správu. U IP-PBX systémů mezi komponenty patří SIP servery, mediální brány a hraniční řadiče relací. Ve specifikacích 3GPP je PBX zmíněna v požadavcích na služby (např. pro podnikové sítě, služby [VPN](/mobilnisite/slovnik/vpn/)) a aspektech zabezpečení, které podrobně popisují, jak rozhraní s prvky [PLMN](/mobilnisite/slovnik/plmn/) (Public Land Mobile Network) zajišťuje bezpečnou a spolehlivou podnikovou komunikaci.

## K čemu slouží

PBX existuje za účelem poskytování efektivní a nákladově efektivní telefonie pro organizace. Před systémy PBX vyžadoval každý telefon vyhrazenou externí linku, což bylo pro interní komunikaci neúměrně drahé a neefektivní. PBX tento problém řeší tím, že umožňuje mnoha interním uživatelům sdílet menší počet externích linek, což výrazně snižuje náklady. Také umožňuje pokročilé telefonní funkce interně, čímž zlepšuje produktivitu podnikání a pracovní postupy komunikace.

Historicky se PBX vyvinula z manuálních ústředen na automatizované digitální systémy. Jejich integrace do standardů 3GPP byla motivována potřebou rozšířit podnikové telefonní služby na mobilní sítě. Když podniky začaly přijímat mobilní zařízení, vznikla poptávka po bezproblémové integraci mezi pevnými kancelářskými telefony a mobilními přístroji, což vedlo ke specifikacím pro vzájemné propojení mezi [PLMN](/mobilnisite/slovnik/plmn/) a privátními podnikovými sítěmi. Tím se řešila omezení, kdy mobilní a pevné sítě fungovaly odděleně, což bránilo jednotné komunikaci.

Specifikace 3GPP definují požadavky a architektury pro propojení PBX, aby zajistily standardizované, bezpečné a interoperabilní podnikové komunikační služby napříč globálními mobilními sítěmi. To podporuje širší průmyslový trend směrem ke Fixed Mobile Convergence a Unified Communications as a Service (UCaaS).

## Klíčové vlastnosti

- Interní přepínání hovorů bez použití externích trunků
- Sdílený přístup k externím linkám PSTN/PLMN
- Privátní číslovací plán a volání na přípony (extenze)
- Pokročilé funkce hovorů (čekání, přesměrování, konferenční hovor, hlasová schránka)
- Integrace se sítěmi 3GPP pro mobilní přípony (extenze)
- Podpora mechanismů zabezpečení a autentizace

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TS 22.519** (Rel-19) — NGN Business Communication Requirements
- **TS 33.790** (Rel-19) — Security for Next-Gen Real-Time Communication Phase 2
- **TS 33.831** (Rel-12) — Study on Spoofed Call Detection & Prevention

---

📖 **Anglický originál a plná specifikace:** [PBX na 3GPP Explorer](https://3gpp-explorer.com/glossary/pbx/)
