---
slug: "naun3"
url: "/mobilnisite/slovnik/naun3/"
type: "slovnik"
title: "NAUN3 – Non-Authenticable Non-3GPP"
date: 2025-01-01
abbr: "NAUN3"
fullName: "Non-Authenticable Non-3GPP"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/naun3/"
summary: "NAUN3 označuje kategorii přístupových sítí Non-3GPP (jako je nedůvěryhodný Wi-Fi), které nemohou provést autentizaci uživatele nebo zařízení vůči 5G core síti. Představuje typ přístupu, u kterého 3GPP"
---

NAUN3 je kategorie přístupových sítí Non-3GPP, jako je nedůvěryhodný Wi-Fi, které se nemohou autentizovat vůči 5G core a vyžadují specifické bezpečnostní procedury.

## Popis

NAUN3 je koncept definovaný ve 3GPP Release 18 v kontextu přístupové bezpečnosti 5G systému. Klasifikuje přístupovou síť Non-3GPP ([N3AN](/mobilnisite/slovnik/n3an/)) na základě její schopnosti podporovat autentizační procedury s 5G Core sítí. Konkrétně je NAUN3 taková N3AN, která nemá funkcionalitu k provedení procedury primární autentizace a dohody o klíči (5G-AKA nebo EAP-AKA') mezi uživatelským zařízením (UE) a Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) v 5G core. Když se UE připojuje přes NAUN3, je k samotné přístupové síti přistupováno jako k nedůvěryhodnému přenosovému médiu. Z tohoto důvodu musí být navázání bezpečného spojení k 5G core dosaženo prostřednictvím [IPsec](/mobilnisite/slovnik/ipsec/) tunelu nebo jiného mechanismu zabezpečeného tunelování, který je ukončen v Non-3GPP InterWorking Function ([N3IWF](/mobilnisite/slovnik/n3iwf/)) v core síti. N3IWF funguje jako bezpečnostní brána. UE nejprve naváže spojení k NAUN3 (např. se asociuje s Wi-Fi [AP](/mobilnisite/slovnik/ap/)) a získá lokální IP adresu. Následně iniciuje proceduru navázání IKEv2/IPsec tunelu s N3IWF. V rámci této IKEv2 výměny je spuštěna autentizační metoda EAP-AKA', která umožňuje vzájemnou autentizaci UE a AUSF prostřednictvím N3IWF. Úspěšná autentizace vede k odvození bezpečnostních klíčů použitých k zabezpečení IPsec tunelu. Veškerý následný uživatelský a řídicí provoz mezi UE a 5G core je přenášen uvnitř tohoto šifrovaného tunelu, což zajišťuje důvěrnost a integritu dat bez ohledu na nedůvěryhodnou a neautentizovatelnou povahu podkladové přístupové sítě.

## K čemu slouží

Koncept NAUN3 byl zaveden, aby formálně uznal a definoval bezpečnostní přístup k široké třídě existujících i budoucích přístupových sítí Non-3GPP, kterým chybí integrované 3GPP autentizační schopnosti. To zahrnuje většinu veřejných, privátních a domácích Wi-Fi sítí, které jsou všudypřítomné, ale nebyly navrženy s ohledem na 3GPP bezpečnostní protokoly. Před touto formální kategorizací 5G systém zacházel se vším přístupem Non-3GPP buď jako s 'důvěryhodným', nebo 'nedůvěryhodným', přičemž nedůvěryhodný přístup vyžadoval tunelování přes [N3IWF](/mobilnisite/slovnik/n3iwf/). NAUN3 upřesňuje kategorii 'nedůvěryhodný' tím, že explicitně označuje neschopnost provádět autentizaci jako klíčovou charakteristiku. Tato formalizace zajišťuje jasné a konzistentní bezpečnostní procedury ve standardech. Řeší praktický problém bezpečné integrace miliard zařízení využívajících Wi-Fi a další necelaulární technologie do služební struktury 5G, aniž by vyžadovala upgrade samotných přístupových sítí. Umožňuje operátorům rozšířit 5G služby přes jakýkoli IP-based přístup při zachování vysokých bezpečnostních standardů 3GPP systému.

## Klíčové vlastnosti

- Klasifikace přístupových sítí Non-3GPP, kterým chybí 3GPP autentizační schopnost
- Ukládá použití N3IWF jako bezpečnostní brány pro připojení k 5G core
- Vyžaduje navázání IPsec tunelu (pomocí IKEv2 s EAP-AKA') mezi UE a N3IWF
- Zajišťuje end-to-end bezpečnost mezi UE a core sítí přes nedůvěryhodný přístupový spoj
- Umožňuje kontinuitu 5G služeb přes široce dostupné přístupy jako standardní Wi-Fi
- Definován v rámci 5G bezpečnostní architektury pro konzistentní aplikaci politik

## Související pojmy

- [N3IWF – Non-3GPP access InterWorking Function](/mobilnisite/slovnik/n3iwf/)

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3

---

📖 **Anglický originál a plná specifikace:** [NAUN3 na 3GPP Explorer](https://3gpp-explorer.com/glossary/naun3/)
