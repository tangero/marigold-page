---
slug: "ajax"
url: "/mobilnisite/slovnik/ajax/"
type: "slovnik"
title: "AJAX – Asynchronous JavaScript and XML"
date: 2025-01-01
abbr: "AJAX"
fullName: "Asynchronous JavaScript and XML"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ajax/"
summary: "AJAX je technika webového vývoje umožňující asynchronní výměnu dat mezi klientskými prohlížeči a servery bez plného obnovení stránky. V rámci 3GPP je standardizována pro tvorbu responzivních webových"
---

AJAX je standardizovaná technika webového vývoje pro mobilní sítě, která umožňuje asynchronní výměnu dat mezi klienty a servery bez nutnosti kompletního obnovení stránky, čímž zlepšuje odezvu a snižuje latenci.

## Popis

AJAX (Asynchronous JavaScript and [XML](/mobilnisite/slovnik/xml/)) je základní webová technologie standardizovaná 3GPP v dokumentu TS 26.938 jako součást rámce Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)). V jádru umožňuje AJAX webovým aplikacím komunikovat se servery asynchronně na pozadí, což umožňuje dynamické aktualizace obsahu bez nutnosti kompletního obnovení stránky. Toho je dosaženo pomocí [API](/mobilnisite/slovnik/api/) XMLHttpRequest (XHR) v JavaScriptu, které může odesílat požadavky [HTTP](/mobilnisite/slovnik/http/)/[HTTPS](/mobilnisite/slovnik/https/) na servery a zpracovávat odpovědi bez blokování interakce uživatele s webovou stránkou.

Architektura aplikací založených na AJAXu sleduje model klient-server, kde klientský JavaScriptový kód běží v uživatelově prohlížeči a komunikuje se serverovými komponentami prostřednictvím asynchronních požadavků. Když uživatel interaguje s webovou stránkou, JavaScriptové funkce mohou spustit objekty XMLHttpRequest k odeslání datových požadavků na server. Server tyto požadavky zpracuje a vrátí data typicky ve formátu XML, [JSON](/mobilnisite/slovnik/json/) nebo prostého textu. Po přijetí odpovědi zpětné volací funkce v JavaScriptu data zpracují a odpovídajícím způsobem aktualizují specifické části Document Object Model ([DOM](/mobilnisite/slovnik/dom/)), zatímco zbytek stránky zůstane nezměněn.

Klíčové komponenty AJAXu zahrnují objekt XMLHttpRequest (nebo moderní Fetch API), který zajišťuje síťovou komunikaci; serverové zpracovatelské komponenty generující odpovědi; a klientský JavaScript, který spravuje životní cyklus požadavku a manipulaci s DOM. Technologie silně spoléhá na zpracování událostí v JavaScriptu pro správu asynchronních operací, využívá zpětné volací funkce, promise nebo vzory async/await ke zpracování odpovědí při jejich příchodu. Toto oddělení aktualizací uživatelského rozhraní od serverové komunikace umožňuje plynulejší uživatelský zážitek.

V sítích 3GPP hraje AJAX klíčovou roli při doručování responzivních webových aplikací přes mobilní připojení. Standardizace v TS 26.938 zajišťuje, že služby založené na AJAXu fungují efektivně v rámci rámce MBMS, zejména pro doručování dynamického obsahu více uživatelům současně. Technologie se integruje s mechanismy Quality of Service (QoS) 3GPP a funkcemi optimalizace sítě, aby minimalizovala dopad časté výměny malých objemů dat na síťové zdroje při zachování responzivity aplikace.

## K čemu slouží

AJAX byl vytvořen, aby řešil omezení tradičních synchronních webových interakcí, kde každá uživatelská akce vyžadovala kompletní obnovení stránky ze serveru. Tento přístup vedl ke špatnému uživatelskému zážitku kvůli znatelným zpožděním, vysoké spotřebě šířky pásma a rušivému obnovování obrazovky. Před AJAXem se webové aplikace potýkaly s poskytováním responzivity srovnatelné s desktopovým softwarem, zejména přes pomalejší mobilní připojení, kde byla omezení latence a šířky pásma výraznější.

Technologie vznikla z potřeby vytvářet interaktivnější a responzivnější webové aplikace, které by mohly konkurovat desktopovému softwaru. Umožněním asynchronní komunikace umožnil AJAX webovým vývojářům vytvářet aplikace, které mohly nezávisle aktualizovat specifické oblasti obsahu, což dramaticky zlepšilo vnímaný výkon. To bylo obzvláště důležité pro mobilní zařízení, kde je prostor na obrazovce omezený a síťové podmínky se výrazně liší.

3GPP standardizoval AJAX ve verzi 12, aby zajistil konzistentní implementaci napříč mobilními sítěmi a zařízeními, a reagoval tak na rostoucí význam webových aplikací v mobilním ekosystému. Standardizace poskytla pokyny pro efektivní implementaci v rámci architektur 3GPP, zejména pro služby [MBMS](/mobilnisite/slovnik/mbms/), kde bylo klíčové efektivní doručování obsahu více uživatelům. Začleněním AJAXu do standardů 3GPP mohla technologie využít síťové optimalizace a bezproblémově spolupracovat s dalšími mobilními službami.

## Klíčové vlastnosti

- Asynchronní komunikace klient-server bez obnovování stránky
- Dynamická manipulace s DOM pro částečné aktualizace stránky
- API XMLHttpRequest pro zpracování požadavků HTTP/HTTPS
- Podpora více datových formátů včetně XML, JSON a prostého textu
- Událostmi řízený programovací model s mechanismy zpětných volání
- Integrace s rámcem 3GPP MBMS pro efektivní doručování obsahu

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [HTTP – Hypertext Transfer Protocol](/mobilnisite/slovnik/http/)

## Definující specifikace

- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks

---

📖 **Anglický originál a plná specifikace:** [AJAX na 3GPP Explorer](https://3gpp-explorer.com/glossary/ajax/)
